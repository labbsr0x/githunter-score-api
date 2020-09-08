import datetime
import logging

import pytz
import schedule
import time
import threading
from githunter.score.models.Schedule import Schedule
from githunter.score.services.agrows_service import get_data

logger = logging.getLogger(__name__)

running: [str] = []


def run(item: Schedule):
    logging.info(f'Schedule item [{item.code}] started.')

    # TODO: Get this from last score from code
    start_date = '2002-10-02T10:00:00-05:00'
    end_date = datetime.datetime.now(pytz.timezone('Brazil/East')).isoformat()

    data = get_data(item.owner, item.thing, item.node, start_date, end_date)

    for user in data:
        attr = user["attributes"]
        score = (2 * int(attr["starsReceived"])) + int(attr["commits"]) + (2 * int(attr["pullRequests"])) + int(
            attr["issuesOpened"]) + (2 * int(attr["contributedRepositories"]))

        print("Name: " + attr["name"] + " Score: " + str(score))

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
