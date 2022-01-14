import dotenv
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    from app.persitence.db import init_db
    init_db(app)

    DebugToolbarExtension(app)

    from app.blueprints.open import bp_open
    app.register_blueprint(bp_open)

    return app


if __name__ == '__main__':
    dotenv.load_dotenv()
    create_app().run()
