from flask import Blueprint, request

from controllers.reserva_controller import (
    criar_reserva_controller,
    listar_reservas_controller,
    buscar_reserva_controller
)

reserva_bp = Blueprint('reserva_bp', __name__, url_prefix='/api/reservas')
@reserva_bp.route('/', methods=['POST'])

def criar_reserva():
    return criar_reserva_controller(request.json)

@reserva_bp.route('/', methods=['GET'])

def listar_reservas():
    return listar_reservas_controller()

@reserva_bp.route('/<int:id>', methods=['GET'])

def buscar_reserva(id):
    return buscar_reserva_controller(id)
 