from flask_restplus import Namespace


class ScoreDto:
    api = Namespace('score', description='score related operations')
    score = api.schema_model('Score', {
        'required': ['score', 'ruler', 'user', 'schedule_code'],
        'properties': {
            'score': {
                'type': 'float',
                'description': 'score'
            },
            'ruler': {
                'type': 'integer',
                'description': 'ruler'
            },
            'user': {
                'type': 'string',
                'description': 'user name'
            },
            'schedule_code': {
                'type': 'string',
                'description': 'schedule code'
            }
        },
        'type': 'object'
    })
