import threading

from githunter.score.utils import setup_util
from githunter.score.scheduler import start
from githunter.score.routes import create_flask_app
from githunter.score.env.environment import env_get_int

if __name__ == '__main__':
    app = create_flask_app()
    setup_util.set_log()
    setup_util.connect_mongo()

    # Start jobs thread
    thread1 = threading.Thread(target=start)
    thread1.start()

    app.run(host='0.0.0.0', port=env_get_int(["app", "port"]), debug=False)


