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

amizade = db.Table(
    "amizade",
    db.Column(
        "primario", db.Integer, db.ForeignKey("user.id"), primary_key=True
    ),
    db.Column(
        "secundario", db.Integer, db.ForeignKey("user.id"), primary_key=True
    ),
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(1000), default="")

    firstname = db.Column(db.String(30), unique=False)
    lastname = db.Column(db.String(120), unique=False)
    email = db.Column(db.String(120), unique=True)
    matricula = db.Column(db.String(30), unique=True)
    telefone = db.Column(db.String(30), unique=True)

    naonulanova = db.Column(db.String(30), nullable=False)

    cursos = db.relationship(
        "Curso", secondary=cursos_alunos, backref=db.backref("users")
    )

    amigos = db.relationship(
        "User",
        secondary=amizade,
        primaryjoin=amizade.c.secundario == id,
        secondaryjoin=amizade.c.primario == id,
        backref="galera",
    )
