import email
from flask import Blueprint, jsonify, request
try:
    from ext.database import db
    from models import User, Curso
except ImportError:
    try:
        from ifbookbackend.ext.database import db
        from ifbookbackend.models import User, Curso
    except ImportError:
        print('Users.py Import Error')

bp = Blueprint("users", __name__, url_prefix="/users", template_folder="templates")


@bp.get("/aluno")
def student():
    return "Welcome!", 200
    

@bp.post("/novo")
def newStudent():
    
    new = User()
    
    new.username = request.form["nome"]
    new.senha = request.form["senha"]

    print(new.username)

    if not new.senha or not new.username:
        return "Nome e/ou Senha vazia", 401

    quem = User.query.filter_by(username=new.username).first()

    if quem :
        return "Username já registrado", 401

    new.descricao = request.form["descricao"]
    new.firstname = request.form["firstname"]
    new.lastname = request.form["lastname"]
    new.email = request.form["email"]
    new.matricula = request.form["matricula"]
    new.telefone = request.form["telefone"]

    db.session.add(new)
    db.session.commit()

    return jsonify({"username": new.username}), 200

def init_app(app):
    app.register_blueprint(bp)
