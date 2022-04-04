import email
from flask import Blueprint, jsonify, request
from ifbookbackend.ext.database import db
from ifbookbackend.models import User

bp_users = Blueprint("users", __name__, url_prefix="/users", template_folder="templates")


@bp_users.get("/")
def student_home():
    return "Welcome!", 200


@bp_users.post("/novo")
def newStudent():
    
    new = User()
    
    new.username = request.form["username"]
    new.senha = request.form["senha"]

    if not new.senha or not new.username:
        return "Nome e/ou Senha vazia", 401

    quem = User.query.filter_by(username=new.username).first()

    if quem :
        return "Username já registrado", 401

    new.descricao = request.form.get("descricao")
    new.firstname = request.form.get("firstname")
    new.lastname = request.form.get("lastname")
    new.email = request.form.get("email")
    new.matricula = request.form.get("matricula")
    new.telefone = request.form.get("telefone")

    db.session.add(new)
    db.session.commit()

    return jsonify({"firstname": new.firstname}), 200

