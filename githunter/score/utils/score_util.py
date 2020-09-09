import math


def get_score(stars, repos, pull_requests, commits, issues):
    return (2 * stars) + (2 * repos) + (2 * pull_requests) + commits + issues


def get_ruler(score):
    if score > 84:
        return 7

    if score < 30:
        return int(math.floor(score / 10)+1)
    if score < 45:
        return 4
    if score < 65:
        return 5

    return 6
