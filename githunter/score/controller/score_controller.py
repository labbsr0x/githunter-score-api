import json

from githunter.score.models.Score import Score
from githunter.score.utils.response_util import get_response, get_success


def get_all():
    try:
        all_scores = Score.objects()
        return get_success(all_scores.to_json())
    except Exception as e:
        return get_response(500, "INTERNAL_ERROR", None, e)


def get_by_username(username: str):
    try:
        items = Score.objects(user=username)\
            .order_by('-updatedAt')\
            .aggregate([{
                '$group': {
                    '_id': '$scheduler_code',
                    'score': {'$first': '$score'},
                    'ruler': {'$first': '$ruler'},
                    'owner': {'$first': '$owner'},
                    'thing': {'$first': '$thing'},
                    'node': {'$first': '$node'},

                }
            }])

        return get_success(json.dumps(list(items)))
    except Exception as e:
        return get_response(500, "INTERNAL_ERROR", None, e)
