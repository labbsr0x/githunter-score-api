from flask_restplus import Namespace


class ScheduleDto:
    api = Namespace('schedule', description='schedule related operations')
    schedule = api.schema_model('Schedule', {
        'required': ['provider', 'node', 'interval_type', 'interval_value'],
        'properties': {
            'provider': {
                'type': 'string',
                'description': 'schedule provider'
            },
            'node': {
                'type': 'string',
                'description': 'schedule node'
            },
            'interval_type': {
                'type': 'string',
                'description': 'schedule interval type: daily, hourly'
            },
            'interval_value': {
                'type': 'integer',
                'description': 'schedule interval value'
            }
        },
        'type': 'object'
    })
