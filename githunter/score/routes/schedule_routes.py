from flask_restplus import Resource
from githunter.score.dto.schedule_dto import ScheduleDto
from githunter.score.controller.schedule_controller import create_new, get_all, remove, get_by_code
from flask import request

schedule_api = ScheduleDto.api
_schedule = ScheduleDto.schedule


@schedule_api.route('/')
class Schedule(Resource):

    @schedule_api.response(200, "OK", [_schedule])
    @schedule_api.doc('list of registered schedules')
    def get(self):
        """List all registered schedules"""
        return get_all()

    @schedule_api.response(200, 'Schedule successfully created.')
    @schedule_api.doc('create a new schedule')
    @schedule_api.expect(_schedule, validate=True)
    def post(self):
        """Creates a new Schedule """
        data = request.json
        return create_new(data=data)


@schedule_api.route('/<schedule_id>')
class ScheduleUnique(Resource):
    @schedule_api.response(200, 'Schedule successfully deleted.')
    @schedule_api.doc('delete a Schedule')
    def delete(self, schedule_id):
        """Delete a Schedule """
        return remove(schedule_id)

    @schedule_api.response(200, "OK", _schedule)
    @schedule_api.doc('get the schedule given its id')
    def get(self, schedule_id):
        """get the schedule given its id"""
        return get_by_code(schedule_id)
