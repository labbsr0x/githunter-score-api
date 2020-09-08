import logging
from githunter.score.env.environment import env_get_str
from mongoengine import connect


def set_log(): logging.basicConfig(level=logging.getLevelName(env_get_str(["app", "log_level"], "INFO")))


def connect_mongo(): connect(host=env_get_str(['db', 'mongo_uri']))
