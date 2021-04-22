import json

from mongoengine import NotUniqueError

from githunter.score.models.ScoreRule import ScoreRule
from githunter.score.utils.response_util import get_response, get_success


def create_new(data: {}) -> {}:
    rule_code = data['rule_code']
    name = data['name']
    math = data['math']
    description = data['description']

    score_rule = ScoreRule(
        rule_code,
        name,
        math,
        description
    )

    try:
        saved = score_rule.save()
        return get_success(saved.to_json())
    except NotUniqueError as e:
        return get_response(409, "SCORE_RULE_ALREADY_EXISTS", None, e)
    except Exception as e:
        return get_response(500, "INTERNAL_ERROR", None, e)


def get_all():
    try:
        all_rules = ScoreRule.objects()
        return get_success(all_rules.to_json())
    except Exception as e:
        return get_response(500, "INTERNAL_ERROR", None, e)


def get_by_rule_id(rule_code: str):
    try:
        items = ScoreRule.objects(rule_code=rule_code) \
            .order_by('-updatedAt')
        if len(items) > 0:
            return get_success(items.to_json())
        return get_response(404, "SCORE_RULE_ITEM_NOT_FOUND")
    except Exception as e:
        return get_response(500, "INTERNAL_ERROR", None, e)


def update_by_rule_id(rule_code: str, data: {}):
    try:
        updated = ScoreRule.objects(rule_code=rule_code)
        if len(updated) > 0:
            name = data['name']
            math = data['math']
            description = data['description']
            updated.update(name=name, math=math, description=description)
            return get_success()
        return get_response(404, "SCORE_RULE_ITEM_NOT_FOUND")
    except Exception as e:
        return get_response(500, "INTERNAL_ERROR", None, e)


def remove(rule_code: str):
    try:
        removed = ScoreRule.objects(rule_code=rule_code).delete()
        if removed > 0:
            return get_success()
        return get_response(404, "SCORE_RULE_ITEM_NOT_FOUND")
    except Exception as e:
        return get_response(500, "INTERNAL_ERROR", None, e)