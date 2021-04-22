from flask_restplus import Resource
from githunter.score.controller.score_rule_controller import get_all, get_by_rule_id, create_new, \
        update_by_rule_id, remove
from githunter.score.dto.score_rule_dto import ScoreRuleDto
from flask import request

score_rule_api = ScoreRuleDto.api
_score_rule = ScoreRuleDto.rule


@score_rule_api.route('/')
class ScoreRules(Resource):

    @score_rule_api.response(200, "OK", [_score_rule])
    @score_rule_api.doc('List of registered scores rules')
    def get(self):
        """List all registered scores"""
        return get_all()

    @score_rule_api.response(200, 'Score Rule successfully created.')
    @score_rule_api.doc('create a new score rule')
    @score_rule_api.expect(_score_rule, validate=True)
    def post(self):
        """Creates a new Score Rule """
        data = request.json
        return create_new(data=data)


@score_rule_api.route('/rule_code/<rule_code>')
class ScoreUnique(Resource):
    @score_rule_api.response(200, "OK", _score_rule)
    @score_rule_api.doc('get the rule by rule_code')
    def get(self, rule_code):
        """get the score rule by rule_code"""
        return get_by_rule_id(rule_code)

    @score_rule_api.response(200, "OK", _score_rule)
    @score_rule_api.doc('update the rule by rule_code')
    def put(self, rule_code):
        """update the score rule by rule_code"""
        data = request.json
        return update_by_rule_id(rule_code, data=data)

    @score_rule_api.response(200, 'Score Rule successfully deleted.')
    @score_rule_api.doc('delete a score rule')
    def delete(self, rule_code):
        """Delete a Rule """
        return remove(rule_code)



