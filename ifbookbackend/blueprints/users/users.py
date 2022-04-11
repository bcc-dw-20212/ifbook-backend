from flask import Blueprint


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/')
def root():
    return 'Hello from users'


def init_app(app):
    app.register_blueprint(bp)