from . import db

class Paciente(db.Model):
    __tablename__ = 'paciente'  

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    prontuario = db.Column(db.String(20), unique=True, nullable=False)

    # Relacionamento com Agendamento
    agendamentos = db.relationship('Agendamento', backref='paciente', lazy=True)
