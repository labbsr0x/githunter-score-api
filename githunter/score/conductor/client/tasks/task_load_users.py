from githunter.score.services.githunter_service import get_users_list


def execute(task):
    print("Starting `load_users` task")

    org = task["inputData"]["organization"]
    provider = task["inputData"]["provider"]
    users_list = get_users_list(org, provider)
    if len(users_list) == 0:
        return {'status': 'FAILED', 'output': {
            'message': f'No User found for organization: {task.input.organization} and provider: {task.input.provider}'}, 'logs': []}

    return {'status': 'COMPLETED', 'output': {'users': users_list}, 'logs': []}
