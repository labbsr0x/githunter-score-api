import datetime
import logging

import pytz
import schedule
import time
import threading
from githunter.score.models.Schedule import Schedule
from githunter.score.models.Score import Score
from githunter.score.services.agrows_service import get_data
from githunter.score.utils.score_util import get_score, calc_metric

logger = logging.getLogger(__name__)

running: [str] = []


def run(item: Schedule):
    logging.info(f'Schedule item [{item.code}] started.')

    tz = pytz.timezone('Brazil/East')
    last_scores = Score.objects(scheduler_code=item.code).order_by(
        '-updatedAt').limit(1000)
    last_score_date = last_scores[0]['updatedAt'].replace(
        tzinfo=tz).isoformat() if len(last_scores) > 0 else None
    lasts = {}

    for last in last_scores:
        if last.user not in lasts:
            lasts[last.user] = last

    start_date = last_score_date if last_score_date is not None else '2002-10-02T10:00:00-05:00'
    end_date = datetime.datetime.now(tz).isoformat()

    data = get_data(item.owner, item.thing, item.node, start_date, end_date)
    scores = {}

    for user in reversed(data):
        attr = user["attributes"]
        name = attr["name"]
        user_name = attr["login"]
        stars = calc_metric(attr, "starsReceived", lasts,
                            user_name, 'stars_received')
        commits = calc_metric(attr, "commits", lasts, user_name, 'commits')
        pull_requests = calc_metric(
            attr, "pullRequests", lasts, user_name, 'pull_requests')
        issues = calc_metric(attr, "issuesOpened", lasts,
                             user_name, 'issues_opened')
        if len(attr["contributedRepositories"]) > 0:
            repos = calc_metric(attr, "contributedRepositories",
                                lasts, user_name, 'contributed_repositories')
        else:
            repos = 0

        score = get_score(stars, repos, pull_requests, commits, issues)

        if user_name not in scores:
            scores[user_name] = Score(
                score,
                name,
                user_name,
                item.owner,
                item.thing,
                item.node,
                item.code,
                stars,
                commits,
                pull_requests,
                issues,
                repos
            ).save()

    logging.info(f'Schedule item [{item.code}] finished.')


def run_threaded(schedule_item):
    thread = threading.Thread(target=run, args=(schedule_item,))
    thread.start()


def remove(code: str):
    schedule.clear(code)


def add(item: Schedule):
    if item.interval_value == 0:
        logging.info(f'Schedule item [{item.code}] will be executed [Now].')

        thread = threading.Thread(target=run, args=(item,))
        thread.start()

    else:
        running.append(item.code)
        interval_value = item.interval_value
        interval_type = item.interval_type

        if interval_type == "daily":
            schedule.every(interval_value).days.do(
                run_threaded, schedule_item=item).tag(item.code)
        elif interval_type == "hourly":
            schedule.every(interval_value).hours.do(
                run_threaded, schedule_item=item).tag(item.code)
        else:
            logging.info(
                f'The param [interval_type] is wrong. You should try: hourly or daily')
            return

        logging.info(
            f'Schedule item [{item.code}] was configured with success. [{interval_type}] [{interval_value}].')


def start():
    items = Schedule.objects()

    for item in items:
        if item.interval_value > 0:
            add(item)

    while True:
        schedule.run_pending()
        time.sleep(10)
