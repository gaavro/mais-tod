from flask import request, current_app, jsonify
from flask_jwt_extended import  jwt_required
from app.exceptions.exceptions import (
    InvalidKeyError,
    InvalidTypeError,
    NotFoundError,
    UniqueUserError,
)
from app.models.customer_model import Customer

@jwt_required()
def create_customer():
    try:
        data = request.get_json()
        Customer.validate_register_args(data)
        customer = Customer(**data)
        current_app.db.session.add(customer)
        current_app.db.session.commit()       
        return jsonify(customer), 201
    except UniqueUserError:
        return {"alerta": "CPF já cadastrado."}, 409
    except InvalidTypeError:
        return {"alerta": "Informações inválidas (apenas texto)."}, 400
    except InvalidKeyError:
        return {
            "alerta": "Informações incorretas (nome, cpf )."
        }, 400


@jwt_required()
def get_all():
    customer = Customer.query.all()
    return jsonify(customer), 200


@jwt_required()
def delete_customer(id):
    current = Customer.query.get(id)
    try:
        Customer.validate_id(current)
    except NotFoundError as e:
        return e.message, 404
    current_app.db.session.delete(current)
    current_app.db.session.commit()
    return "", 204
