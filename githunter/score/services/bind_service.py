import json
import logging

import requests

from githunter.score.config import CONFIG

logger = logging.getLogger(__name__)
bind_url = CONFIG["BIND"]["URL"]


def get_data(provider: str, node: str, start_date: str, end_date: str):
    data_api_url = f'{bind_url}?/provider={provider}&node={node}'
    data_api_params = {
        'startDateTime': start_date,
        'endDateTime': end_date
    }

    headers = {
        'content-type': 'application/json',
    }

    request = requests.get(data_api_url, params=data_api_params, headers=headers)

    return json.loads(request.text)['data']
