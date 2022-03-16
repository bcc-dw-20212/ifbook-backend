from ifbookbackend.ext.database import db


class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), unique=True, nullable=False)
    sigla = db.Column(db.String(4), unique=True)


cursos_alunos = db.Table(
    "cursos_alunos",
    db.Column("aluno", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("curso", db.Integer, db.ForeignKey("curso.id"), primary_key=True),
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(1000), default="")

    cursos = db.relationship(
        "Curso", secondary=cursos_alunos, backref=db.backref("users")
    )
