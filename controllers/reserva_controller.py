from flask import jsonify
from models.reserva_model import Reserva
from app.database import db

# Simula cache de turmas
turmas_cache = {}
import requests, threading

def atualizar_cache_turmas():
    global turmas_cache
    try:
        url = "http://localhost:5000/turmas"
        resp = requests.get(url)

        if resp.status_code == 200:
            turmas = resp.json().get("data", {}).get("turmas", [])
            turmas_cache = {t['id']: t for t in turmas}

        else:
            print(f"Erro ao obter turmas: {resp.status_code}")

    except Exception as e:
        print(f"Erro: {e}")

    threading.Timer(600, atualizar_cache_turmas).start()
atualizar_cache_turmas()

def validar_turma(turma_id):
    return turma_id in turmas_cache

def criar_reserva_controller(data):
    turma_id = data.get('turma_id')

    if turma_id is None:
        return jsonify({'erro': 'O campo turma_id é obrigatório'}), 400
    
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
    turma = turmas_cache.get(turma_id)

    return jsonify({
        'mensagem': 'Reserva criada com sucesso',

        'reserva': {

            'id': reserva.id,

            'sala': reserva.sala,

            'data': reserva.data,

            'hora_inicio': reserva.hora_inicio,

            'hora_fim': reserva.hora_fim,

            'turma': turma

        }

    }), 201

def listar_reservas_controller():
    reservas = Reserva.query.all()
    resultado = []

    for r in reservas:
        turma = turmas_cache.get(r.turma_id)

        resultado.append({

            'id': r.id,

            'sala': r.sala,

            'data': r.data,

            'hora_inicio': r.hora_inicio,

            'hora_fim': r.hora_fim,

            'turma': turma

        })

    return jsonify(resultado)

def buscar_reserva_controller(id):
    reserva = Reserva.query.get_or_404(id)
    turma = turmas_cache.get(reserva.turma_id)

    return jsonify({

        'id': reserva.id,

        'sala': reserva.sala,

        'data': reserva.data,

        'hora_inicio': reserva.hora_inicio,

        'hora_fim': reserva.hora_fim,

        'turma': turma

    })
 