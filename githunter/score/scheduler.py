import datetime
import logging

import pytz
import schedule
import time
import threading
from githunter.score.models.Schedule import Schedule
from githunter.score.models.Score import Score
from githunter.score.services.agrows_service import get_data
from githunter.score.utils.score_util import get_score

logger = logging.getLogger(__name__)

running: [str] = []


def run(item: Schedule):
    logging.info(f'Schedule item [{item.code}] started.')

    tz = pytz.timezone('Brazil/East')
    last_score = Score.objects(scheduler_code=item.code).order_by('-updatedAt').limit(1)
    last_score_date = last_score[0]['updatedAt'].replace(tzinfo=tz).isoformat() if len(last_score) > 0 else None

    start_date = last_score_date if last_score_date is not None else '2002-10-02T10:00:00-05:00'
    end_date = datetime.datetime.now(tz).isoformat()

    data = get_data(item.owner, item.thing, item.node, start_date, end_date)

    for user in data:
        attr = user["attributes"]
        stars = int(attr["starsReceived"])
        commits = int(attr["commits"])
        pull_requests = int(attr["pullRequests"])
        issues = int(attr["issuesOpened"])
        repos = int(attr["contributedRepositories"])
        user_name = attr["name"]
        score = get_score(stars, repos, pull_requests, commits, issues)

        Score(score, user_name, item.owner, item.thing, item.node, item.code).save()

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
            schedule.every(interval_value).days.do(run_threaded, schedule_item=item).tag(item.code)
        elif interval_type == "hourly":
            schedule.every(interval_value).hours.do(run_threaded, schedule_item=item).tag(item.code)
        else:
            logging.info(f'The param [interval_type] is wrong. You should try: hourly or daily')
            return

        logging.info(f'Schedule item [{item.code}] was configured with success. [{interval_type}] [{interval_value}].')


def start():
    items = Schedule.objects()

    for item in items:
        if item.interval_value > 0:
            add(item)

    while True:
        schedule.run_pending()
        time.sleep(10)
