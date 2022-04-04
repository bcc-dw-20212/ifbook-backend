from flask import Flask
from ifbookbackend.ext import configuration
from .views import root

from ifbookbackend.blueprints.users.users import bp_users


def create_app() -> Flask:
    app = Flask(__name__)
    configuration.init_app(app)
    
    app.register_blueprint(bp_users)

    app.add_url_rule("/", view_func=root)

    return app
