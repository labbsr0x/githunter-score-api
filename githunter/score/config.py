import os
from dotenv import load_dotenv
from os.path import join, dirname

if not os.getenv("SCORE_ENVIRONMENT"):
    load_dotenv(dotenv_path=join(dirname(__file__), '../../.local.env'))

CONFIG = {
    "DB": {
        "MONGO_URI": os.environ['DB_MONGO_URI']
    },
    "BIND": {
      "URL": os.environ['BIND_URL']
    },
    "APP": {
        "LOG_LEVEL": os.environ['APP_LOG_LEVEL'],
        "PORT": os.environ['APP_PORT']
    }
}
