import logging
from githunter.score.config import CONFIG
from mongoengine import connect


def set_log(): logging.basicConfig(level=logging.getLevelName(CONFIG["APP"]["LOG_LEVEL"]))


def connect_mongo(): connect(host=CONFIG["DB"]["MONGO_URI"])
