import threading

from githunter.score.config import CONFIG
from githunter.score.utils import setup_util
from githunter.score.routes import create_flask_app
from githunter.score.conductor.client.register_tasks import register_tasks

if __name__ == '__main__':
    app = create_flask_app()
    setup_util.set_log()
    setup_util.connect_mongo()

    # Start Conductor
    register_tasks()

    app.run(host='0.0.0.0', port=CONFIG["APP"]["PORT"], debug=False)


