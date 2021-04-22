from flask_restplus import Namespace


class ScoreRuleDto:
    api = Namespace('rule', description='score rule related operations')
    rule = api.schema_model('Rule', {
        'required': ['rule_code', 'name', 'math'],
        'properties': {
            'rule_code': {
                'type': 'string',
                'description': 'the code of the rule'
            },
            'name': {
                'type': 'string',
                'description': 'the name of the rule'
            },
            'description': {
                'type': 'string',
                'description': 'a description of the rule'
            },
            'math': {
                'type': 'string',
                'description': 'math to be `eval`. Known variables: stars, repos, pull_requests, commits, issues'
            }
        },
        'type': 'object'
    })
