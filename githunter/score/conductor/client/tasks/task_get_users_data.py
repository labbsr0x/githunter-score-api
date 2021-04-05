import datetime
import pytz

from githunter.score.services.githunter_service import get_user


def execute(task):
    print("Starting `get_users_data` task")

    tz = pytz.timezone('Brazil/East')

    start_date = '2002-10-02T10:00:00-03:00'
    end_date = datetime.datetime.now(tz).isoformat()

    users_list = task["inputData"]["users"]

    data = []
    for user in users_list:

        user_score = get_user(user["login"], user["provider"], start_date, end_date)
        if user_score is not None:
            data.append(user_score)

    if len(data) == 0:
        return {'status': 'FAILED', 'output': {
            'message': 'No User Data found '}, 'logs': []}

    return {'status': 'COMPLETED', 'output': {'users': data}, 'logs': []}
