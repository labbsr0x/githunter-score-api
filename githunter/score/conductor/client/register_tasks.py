from __future__ import print_function

import pathlib
from conductor.ConductorWorker import ConductorWorker
import os
from githunter.score.config import CONFIG

conductor_url = CONFIG["CONDUCTOR"]["URL"]

cc = ConductorWorker(conductor_url, 1, 0.1)


def Conductor():
    return cc


def start(m):
    print("reg")
    print(m)
    cc.start('scraper_comments', m.execute, False)


def register_tasks():
    print('Register Tasks in Conductor:')
    files = list(filter(lambda x: x.startswith('task_'), os.listdir(pathlib.Path(__file__).parent / 'tasks')))
    tasks = list(map(lambda x: x.split(".py")[0], files))
    print(tasks)
    module_names = list(map(lambda x: f'githunter.score.conductor.client.tasks.{x.split(".py")[0]}', files))
    modules = list(map(__import__, module_names))
    tasks_modules = dict(zip(tasks, modules))
    for t, m in tasks_modules.items():
        executeFunc = eval(f'm.score.conductor.client.tasks.{t}.execute')
        cc.start(f'us_{t.split("task_")[1]}', executeFunc, False)

