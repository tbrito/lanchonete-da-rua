from .. import db

class Cliente(db.Model):
    """ Modelo Cliente """
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    nome = db.Column(db.String(50), unique=True)
    telefone = db.Column(db.String(50), unique=True)
    