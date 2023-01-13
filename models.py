from app import db
from sqlalchemy.orm import backref

class Obras(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    nome = db.Column(db.String(100), nullable=False)

    autor = db.Column(db.String(100), nullable=False)

    ano_criacao = db.Column(
        db.Integer,
    )

    propietario = db.Column(db.String(100))

    url = db.Column(db.String(999))

    def __init__(self, nome, autor, ano_criacao, propietario, url) -> None:
        self.nome = nome
        self.autor = autor
        self.ano_criacao = ano_criacao
        self.url = url
        self.propietario = propietario

    @staticmethod
    def create(nome, autor, ano_criacao, propietario, url,) -> None:
        new_obra = Obras(nome, autor, ano_criacao, propietario, url)
        db.session.add(new_obra)

        db.session.commit()

    def __repr__(self):
        return "<Name %r>" % self.nome

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    senha = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return "<Name %r>" % self.nome

    def __init__(self, nome, username, senha) -> None:
        self.nome = nome
        self.username = username
        self.senha = senha

    @staticmethod
    def create(nome, username, senha):
        new_user = User(nome, username, senha)

        db.session.add(new_user)
        db.session.commit()