from flask_restplus import Resource
from githunter.score.controller.score_controller import get_all, get_by_username, get_by_username_and_date_range
from githunter.score.dto.score_dto import ScoreDto
from flask import request

score_api = ScoreDto.api
_score = ScoreDto.score


@score_api.route('/')
class Score(Resource):

    @score_api.response(200, "OK", [_score])
    @score_api.doc('list of registered scores')
    def get(self):
        """List all registered scores"""
        return get_all()


@score_api.route('/user/<username>')
class ScoreUnique(Resource):
    @score_api.response(200, "OK", _score)
    @score_api.doc('get the score by user_name')
    def get(self, username):
        """get the score by user_name"""
        return get_by_username(username)


@score_api.route('/user/<username>/score')
class ScoreUnique(Resource):
    @score_api.response(200, "OK", _score)
    @score_api.doc('get the score by user_name')
    def get(self, username):
        """get the score by user_name"""
        return get_by_username_and_date_range(username, request.args.to_dict())