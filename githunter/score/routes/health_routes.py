from flask_restplus import Namespace, Resource

health_api = Namespace('health', description='health related operations')


@health_api.route('/')
class Health(Resource):
    @health_api.doc('api to check if scraper is up')
    def get(self):
        return {
            "status": "up"
        }
