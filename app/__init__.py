import dotenv
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    from app.persitence.db import init_db
    init_db(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_email):
        from app.controllers.user_controller import get_user_by_email
        return get_user_by_email(user_email)
    #DebugToolbarExtension(app)

    from app.blueprints.open import bp_open
    app.register_blueprint(bp_open)

    from app.blueprints.users import bp_user
    app.register_blueprint(bp_user)

    from app.blueprints.admin import bp_admin
    app.register_blueprint(bp_admin)

    return app


if __name__ == '__main__':
    dotenv.load_dotenv()
    create_app().run()
