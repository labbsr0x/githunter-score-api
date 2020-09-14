from flask import Flask
from flask_restplus import Api
from githunter.score.routes.health_routes import health_api
from githunter.score.routes.schedule_routes import schedule_api
from githunter.score.routes.score_routes import score_api


def create_flask_app():
    app = Flask(__name__)

    api = Api(
        app,
        version='1.0',
        title='Score API',
        description='A service that calculates the user score.',
    )

    api.add_namespace(schedule_api)
    api.add_namespace(health_api)
    api.add_namespace(score_api)

    return app
