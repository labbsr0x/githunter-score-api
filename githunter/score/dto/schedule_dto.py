from flask_restplus import Namespace


class ScheduleDto:
    api = Namespace('schedule', description='schedule related operations')
    schedule = api.schema_model('Schedule', {
        'required': ['owner', 'thing', 'node', 'interval_type', 'interval_value'],
        'properties': {
            'owner': {
                'type': 'string',
                'description': 'schedule agrows owner'
            },
            'thing': {
                'type': 'string',
                'description': 'schedule agrows thing'
            },
            'node': {
                'type': 'string',
                'description': 'schedule agrows node'
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
