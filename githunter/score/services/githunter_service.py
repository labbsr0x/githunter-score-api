import json
import logging

import requests

from githunter.score.config import CONFIG

logger = logging.getLogger(__name__)
githunter_url = CONFIG["GITHUNTER"]["URL"]
user_endpoint = CONFIG["GITHUNTER"]["ENDPOINTS"]["USER"]
user_simple_endpoint = CONFIG["GITHUNTER"]["ENDPOINTS"]["USER_SIMPLE"]


def get_user(author: str, author_provider: str, start_date: str, end_date: str):
    data_api_url = f'{githunter_url}{user_endpoint}?author={author}&authorProvider={author_provider}' \
                   f'&startDateTime={start_date}&endDateTime={end_date}'

    headers = {
        'content-type': 'application/json',
    }

    request = requests.get(data_api_url, headers=headers)

    if request.status_code != 200:
        logging.info(f'No data found in Githunter-Api for user {author} on provider {author_provider}')
        return None
    else:
        return json.loads(request.text)['data']


def get_users_list():
    data_api_url = f'{githunter_url}{user_simple_endpoint}'

    headers = {
        'content-type': 'application/json',
    }

    request = requests.get(data_api_url, headers=headers)

    if request.status_code != 200:
        logging.info(f'No data found in Githunter-Api')
        return None
    else:
        return json.loads(request.text)['users']