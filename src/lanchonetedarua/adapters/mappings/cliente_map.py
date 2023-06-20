from application import db

import datetime

class Cliente(db.Model):
    id = nome = db.Column(
        db.Integer, primary_key=True,
        unique=True, nullable=False)
    nome = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String, nullable=True)
    telefone = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, nome: str, cpf: str = ''):
        self.nome = nome
        self.cpf = cpf