import math


def get_score(stars, repos, pull_requests, commits, issues):
    return (2 * stars) + (2 * repos) + (2 * pull_requests) + commits + issues


def get_ruler(score):
    if score > 84:
        return 7

    if score < 30:
        return int(math.floor(score / 10) + 1)
    if score < 45:
        return 4
    if score < 65:
        return 5

    return 6


def calc_metric(new_user, new_user_metric, lasts, user_name, last_user_metric):
    if user_name in lasts and new_user[new_user_metric] and lasts[user_name] and lasts[user_name][last_user_metric]:
        return int(lasts[user_name][last_user_metric])-int(new_user[new_user_metric])
    return int(new_user[new_user_metric])


def calc_diff(newer_data, older_data, metric_name):
    if metric_name in newer_data and metric_name in older_data:
        return int(newer_data[metric_name])-int(older_data[metric_name])
    return int(newer_data[metric_name])