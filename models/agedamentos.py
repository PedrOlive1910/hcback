from . import db
from datetime import date

class Agendamento(db.Model):
    __tablename__ = 'agendamento'  

    id = db.Column(db.Integer, primary_key=True)
    data_agendamento = db.Column(db.Date, nullable=False, default=date.today)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)

    def __repr__(self):
        return f'<Agendamento {self.data_agendamento} - {self.paciente_id}>'
