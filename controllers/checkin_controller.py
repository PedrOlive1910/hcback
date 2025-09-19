from flask import request, jsonify
from models import db
from models.paciente import Paciente
from datetime import datetime

from flask import Blueprint
checkin_bp = Blueprint('checkin', __name__)

@checkin_bp.route('/checkin', methods=['POST'])
def checkin():
    dados = request.get_json()
    identificador = dados.get('identificador')  # Pode ser QR, CPF ou prontuario
    local = dados.get('local')

    paciente = Paciente.query.filter(
        (Paciente.cpf == identificador) | (Paciente.prontuario == identificador)
    ).first()
    if not paciente:
        return jsonify({'status': 'erro', 'mensagem': 'Paciente não encontrado.'}), 404

    now = datetime.now()
    paciente.checkin_time = now
    paciente.checkin_local = local
    db.session.commit()

    destino = 'triagem'
    orientacoes = f"Dirija-se à {destino}"
    return jsonify({
        'status': 'sucesso',
        'mensagem': 'Check-in realizado!',
        'orientacoes': orientacoes,
        'data': now.strftime('%d/%m/%Y'),
        'hora': now.strftime('%H:%M:%S')
    })
