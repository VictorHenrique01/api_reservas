from flask import Blueprint, jsonify, request
from reserva_model import Reserva
from database import db
import requests

reserva_bp = Blueprint('reserva_bp', __name__)

# Função para validar se a turma existe na API principal
def validar_turma(turma_id):
    url = f"http://localhost:5000/turmas/{turma_id}"
    resp = requests.get(url)
    print(f"Validando turma com ID {turma_id} - Status: {resp.status_code}")
    return resp.status_code == 200


# Rota para criar uma nova reserva
@reserva_bp.route('/reservas', methods=['POST'])
def criar_reserva():
    data = request.json
    turma_id = data.get('turma_id')

    if not validar_turma(turma_id):
        return jsonify({'erro': 'Turma não encontrada'}), 400

    reserva = Reserva(
        sala=data.get('sala'),
        data=data.get('data'),
        hora_inicio=data.get('hora_inicio'),
        hora_fim=data.get('hora_fim'),
        turma_id=turma_id
    )
    db.session.add(reserva)
    db.session.commit()
    return jsonify({'mensagem': 'Reserva criada com sucesso'}), 201

# Rota para listar todas as reservas
@reserva_bp.route('/reservas', methods=['GET'])
def listar_reservas():
    reservas = Reserva.query.all()
    return jsonify([
        {
            'id': r.id,
            'sala': r.sala,
            'data': r.data,
            'hora_inicio': r.hora_inicio,
            'hora_fim': r.hora_fim,
            'turma_id': r.turma_id
        } for r in reservas
    ])

# Rota para buscar uma reserva específica
@reserva_bp.route('/reservas/<int:id>', methods=['GET'])
def buscar_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    return jsonify({
        'id': reserva.id,
        'sala': reserva.sala,
        'data': reserva.data,
        'hora_inicio': reserva.hora_inicio,
        'hora_fim': reserva.hora_fim,
        'turma_id': reserva.turma_id
    })
