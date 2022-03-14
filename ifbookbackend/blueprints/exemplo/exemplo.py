from flask import Blueprint

from ifbookbackend.ext.database import db
from ifbookbackend.models import User

bp = Blueprint("exemplo", __name__, url_prefix="/exemplo", template_folder="templates")


@bp.route("/")
def root():
    busca = "eli"
    usuario = User.query.filter_by(username=f"%{busca}%").first()
    return f"nome: {usuario.username} <br>Senha: {usuario.senha}"


@bp.route("/<nome>/<senha>")
def salva(nome, senha):
    novo = User()
    novo.username = nome
    novo.senha = senha

    db.session.add(novo)
    db.session.commit()

    return "deu certo"


def init_app(app):
    app.register_blueprint(bp)
