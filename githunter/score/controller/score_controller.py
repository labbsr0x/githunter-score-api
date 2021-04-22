import json

from githunter.score.models.ScoreRule import ScoreRule
from githunter.score.models.Score import Score
from githunter.score.utils.response_util import get_response, get_success
from githunter.score.utils.score_util import get_score, calc_diff, get_ruler


def get_all():
    try:
        all_scores = Score.objects()
        return get_success(all_scores.to_json())
    except Exception as e:
        return get_response(500, "INTERNAL_ERROR", None, e)


def get_by_username(username: str, params: dict):
    try:
        if params.get("startDateTime") is not None:
            items = Score.objects(user=username, updatedAt__gte=params["startDateTime"],
                                  updatedAt__lt=params["endDateTime"]).order_by('-updatedAt')
        else:
            items = Score.objects(user=username).order_by('-updatedAt')

        score_rule = ScoreRule.objects(rule_code=params["rule_code"])
        if len(items) < 0:
            return get_response(404, "SCORE_RULE_ITEM_NOT_FOUND")
        score_rule = score_rule.get(0)

        user_list = list(items)
        if len(user_list) < 2:
            return get_success(json.dumps(list(items)))

        newer = user_list[0]
        older = user_list[-1]

        user = {"name": newer["name"], "login": newer["user"], "provider": newer["provider"],
                "starsReceived": calc_diff(newer, older, 'stars_received'),
                "commits": calc_diff(newer, older, 'commits'), "pullRequests": calc_diff(newer, older, 'pull_requests'),
                "issuesOpened": calc_diff(newer, older, 'issues_opened'),
                "contributedRepositories": calc_diff(newer, older, 'contributed_repositories')}

        user["score"] = get_score(score_rule["math"], user["starsReceived"], user["contributedRepositories"],
                                  user["pullRequests"], user["commits"], user["issuesOpened"])
        user["ruler"] = get_ruler(user["score"])

        return get_success(json.dumps(user))
    except Exception as e:
        return get_response(500, "INTERNAL_ERROR", None, e)