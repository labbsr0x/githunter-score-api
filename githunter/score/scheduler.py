import datetime
import logging

import pytz
import schedule
import time
import threading
from githunter.score.models.Schedule import Schedule
from githunter.score.models.Score import Score
from githunter.score.services.githunter_service import get_users_list, get_user
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

    data = []
    users_list = get_users_list()

    if users_list:
        for user in users_list:
            user_score = get_user(user["login"], user["provider"], start_date, end_date)
            data.append(user_score)

    scores = {}

    if len(data) > 0:
        for user in data:
            name = user["name"]
            user_name = user["login"]
            provider = user["provider"]
            stars = calc_metric(user, "starsReceived", lasts,
                                user_name, 'stars_received')
            commits = calc_metric(user, "commits", lasts, user_name, 'commits')
            pull_requests = calc_metric(
                user, "pullRequests", lasts, user_name, 'pull_requests')
            issues = calc_metric(user, "issuesOpened", lasts,
                                 user_name, 'issues_opened')
            repos = calc_metric(user, "contributedRepositories",
                                lasts, user_name, 'contributed_repositories')

            score = get_score(stars, repos, pull_requests, commits, issues)

            if user_name not in scores:
                scores[user_name] = Score(
                    score,
                    name,
                    user_name,
                    provider,
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
