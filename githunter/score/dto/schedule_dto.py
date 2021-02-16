from flask_restplus import Namespace


class ScheduleDto:
    api = Namespace('schedule', description='schedule related operations')
    schedule = api.schema_model('Schedule', {
        'required': ['code', 'interval_type', 'interval_value'],
        'properties': {
            'code': {
                'type': 'string',
                'description': 'code that sets the schedule'
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
