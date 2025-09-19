from flask import Blueprint, request, jsonify
from services.paciente_service import verificar_paciente
from models import db
from models.paciente import Paciente

pacientes_bp = Blueprint('pacientes', __name__)


@pacientes_bp.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    cpf = dados.get('cpf')
    prontuario = dados.get('prontuario')

    resultado = verificar_paciente(cpf, prontuario)
    return jsonify(resultado)


@pacientes_bp.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.get_json()
    nome = dados.get('nome')
    cpf = dados.get('cpf')
    prontuario = dados.get('prontuario')

   
    existente = Paciente.query.filter(
        (Paciente.cpf == cpf) | (Paciente.prontuario == prontuario)
    ).first()
    if existente:
        return jsonify({'status': 'erro', 'mensagem': 'Paciente já cadastrado.'})

    # Cria e salva novo paciente
    paciente = Paciente(nome=nome, cpf=cpf, prontuario=prontuario)
    db.session.add(paciente)
    db.session.commit()

    return jsonify({'status': 'sucesso', 'mensagem': 'Paciente cadastrado!', 'paciente_id': paciente.id})
