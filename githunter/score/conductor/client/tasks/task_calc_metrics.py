from githunter.score.utils.score_util import get_score


def execute(task):
    print("Starting `calc_metrics` task")

    users_list = task["inputData"]["users"]

    if users_list is None or len(users_list) == 0:
        return {'status': 'FAILED', 'output': {
            'message': f'No User found'}, 'logs': []}

    for user in users_list:
        user['score'] = get_score(user["starsReceived"], user["contributedRepositories"], user["pullRequests"],
                                  user["commits"],
                                  user["issuesOpened"])

    return {'status': 'COMPLETED', 'output': {'users': users_list}, 'logs': []}
