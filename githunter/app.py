import threading

from githunter.score.config import CONFIG
from githunter.score.utils import setup_util
from githunter.score.scheduler import start
from githunter.score.routes import create_flask_app

if __name__ == '__main__':
    app = create_flask_app()
    setup_util.set_log()
    setup_util.connect_mongo()

    # Start jobs thread
    thread1 = threading.Thread(target=start)
    thread1.start()

    app.run(host='0.0.0.0', port=CONFIG["APP"]["PORT"], debug=False)


