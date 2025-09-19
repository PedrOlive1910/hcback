from . import db

class Paciente(db.Model):
    __tablename__ = 'paciente'  

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    prontuario = db.Column(db.String(20), unique=True, nullable=False)

    checkin_time = db.Column(db.DateTime, nullable=True)
    checkin_local = db.Column(db.String(100), nullable=True)

    # Relacionamento com Agendamento
    agendamentos = db.relationship('Agendamento', backref='paciente', lazy=True)
