from models.paciente import Paciente    
from models.agedamentos import Agendamento
from models import db 
from datetime import date

def verificar_paciente(cpf, prontuario):
    paciente = Paciente.query.filter_by(cpf=cpf, prontuario=prontuario).first()

    if not paciente:
        return {'status': 'erro', 'mensagem': 'Paciente não encontrado.'}
    
    agendamento = Agendamento.query.filter_by(
        paciente_id=paciente.id, data_agendamento=date.today()
        ).first()
    if Agendamento:
        return {'status': 'sucesso', 'mensagem': 'Paciente autenticado com sucesso.', 'paciente_id': paciente.id}
    else:
        return {'status': 'erro', 'mensagem': 'Nenhum agendamento encontrado para hoje.'}