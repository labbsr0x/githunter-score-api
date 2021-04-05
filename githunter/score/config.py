import os
from dotenv import load_dotenv
from os.path import join, dirname

if not os.getenv("SCORE_ENVIRONMENT"):
    load_dotenv(dotenv_path=join(dirname(__file__), '../../.local.env'))

CONFIG = {
    "DB": {
        "MONGO_URI": os.environ['DB_MONGO_URI']
    },
    "GITHUNTER": {
        "URL": os.environ['GITHUNTER_API_URL'],
        "ENDPOINTS": {
            "USER": os.environ['GITHUNTER_USER_ENDPOINT'],
            "USER_SIMPLE": os.environ['GITHUNTER_USER_SIMPLE_ENDPOINT']
        }
    },
    "APP": {
        "LOG_LEVEL": os.environ['APP_LOG_LEVEL'],
        "PORT": os.environ['APP_PORT']
    },
    "CONDUCTOR": {
        "URL": os.environ['CONDUCTOR_URL']
    }
}
