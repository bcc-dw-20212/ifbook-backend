from flask import Blueprint, jsonify, request

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)

from ifbookbackend.ext.database import db
from ifbookbackend.models import User, Curso

bp = Blueprint("exemplo", __name__, url_prefix="/exemplo", template_folder="templates")


@bp.route("/<busca>")
def root(busca):
    print("oi oi oi")
    usuario = User.query.filter_by(username=busca).first()
    cursos = ""
    for curso in usuario.cursos:
        cursos += f"{curso.sigla}, "

    amigos = ""
    for amigo in usuario.amigos:
        amigos += f"{amigo.username}, "
    return f"nome: {usuario.username} <br>Cursos: {cursos}<br>Amigos: {amigos}"


@bp.route("/alunosdocurso/<s>")
def alunosdocurso(s):
    curso = Curso.query.filter_by(sigla=s).first()

    if curso:
        resposta = ""
        for usuario in curso.users:
            resposta += f"{usuario.username}, "
        return resposta
    else:
        return "Curso não existe", 404


@bp.route("/addcurso/<nome>/<sigla>")
def salvaCurso(nome, sigla):
    novo = Curso()
    novo.nome = nome
    novo.sigla = sigla

    db.session.add(novo)
    db.session.commit()

    return "Curso cadastrado"


@bp.route("/adduser/<nome>/<senha>/<descricao>/<int:curso_id>")
def salva(nome, senha, descricao, curso_id):
    novo = User()
    novo.username = nome
    novo.senha = senha
    novo.descricao = descricao

    curso_da_pessoa = Curso.query.get(curso_id)

    if curso_da_pessoa:
        novo.cursos.append(curso_da_pessoa)
    else:
        return "Da próxima vez vá se cadastrar sem curso na casa da sua avó.", 400

    db.session.add(novo)
    db.session.commit()

    return "deu certo"


@bp.route("/novocurso/<int:ida>/<int:idb>")
def novocurso(ida, idb):
    pessoa = User.query.get(ida)

    novocurso = Curso.query.get(idb)

    pessoa.cursos.append(novocurso)

    db.session.add(pessoa)
    db.session.commit()

    return "Você tem um novo curso."


@bp.route("/amigos/<int:ida>/<int:idb>")
def amigos(ida, idb):
    eu = User.query.get(ida)
    meuAmigo = User.query.get(idb)

    eu.amigos.append(meuAmigo)

    db.session.add(eu)
    db.session.commit()

    return "São amigos"


@bp.post("/login")
def login_user():
    nome = request.form["nome"]
    senha = request.form["senha"]

    quem = User.query.filter_by(username=nome).first()

    if not quem:
        return "Usuário não existente", 404

    if quem.senha == senha:
        token_acesso = create_access_token(identity=quem.username)
        token_refresh = create_refresh_token(identity=quem.id)

        return jsonify({"access_token": token_acesso, "refresh_token": token_refresh})

    return "Senha não confere", 404


@bp.get("/protegida")
@jwt_required()
def protegida():
    usuario = get_jwt_identity()
    print(usuario)
    return "usuario", 200


def init_app(app):
    app.register_blueprint(bp)
