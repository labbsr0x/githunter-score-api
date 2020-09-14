import json
import logging

import requests

from githunter.score.config import CONFIG

logger = logging.getLogger(__name__)
auth_uri = CONFIG["AGROWS"]["AUTH_URI"]
data_uri = CONFIG["AGROWS"]["DATA_API_URI"]
auth_client_id = CONFIG["AGROWS"]["AUTH_ID"]
auth_client_secret = CONFIG["AGROWS"]["AUTH_SECRET"]


def get_token():
    auth_data = {
        'client_id': auth_client_id,
        'client_secret': auth_client_secret,
        'grant_type': 'client_credentials'
    }

    auth_headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    req = requests.post(auth_uri, data=auth_data, headers=auth_headers)

    return json.loads(req.text)['access_token']


def get_data(owner: str, thing: str, node: str, start_date: str, end_date: str):
    token = get_token()
    data_api_url = f'{data_uri}/owner/{owner}/thing/{thing}/node/{node}'
    data_api_params = {
        'startDateTime': start_date,
        'endDateTime': end_date
    }

    data_api_headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    data_api_request = requests.get(data_api_url, params=data_api_params, headers=data_api_headers)

    return json.loads(data_api_request.text)['data']
