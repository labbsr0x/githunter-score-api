from githunter.score.models.Score import Score


def execute(task):
    print("Starting `save_mongo` task")

    users_list = task["inputData"]["users"]

    if users_list is None or len(users_list) == 0:
        return {'status': 'FAILED', 'output': {
            'message': f'No User found'}, 'logs': []}

    scores = {}
    for user in users_list:

        if user["login"] not in scores:
            scores[user["login"]] = Score(
                user["score"],
                user["name"],
                user["login"],
                user["provider"],
                f'{user["provider"]}_{user["login"]}', # code
                user["starsReceived"],
                user["commits"],
                user["pullRequests"],
                user["issuesOpened"],
                user["contributedRepositories"]
            ).save()

    return {'status': 'COMPLETED', 'output': {}, 'logs': []}


