from flask import request, current_app, jsonify
from flask_jwt_extended.utils import get_jwt_identity
from app.exceptions.exceptions import (
    InvalidKeyError,
    InvalidTypeError,
    NotFoundError,
    ProductAlreadyExistsError,
)
from app.models.products_model import Products
from flask_jwt_extended import jwt_required

@jwt_required()
def register_products():
    try:
        data = request.get_json()
        current_store = get_jwt_identity()
        if 'cnpj' not in current_store:
            return {'alerta':'Usuário não autorizado para cadastrar produto'}, 401

        Products.validate_keys(data)
        product = Products(**data)
        current_app.db.session.add(product)
        current_app.db.session.commit()
        return jsonify(product),201
      
    except InvalidKeyError:
        return {
            "alert": "Chave inválida! Deve conter somente as chaves:name, value."
        }, 409
    except InvalidTypeError:
        return {
            "alert": "informações incorretas"
        }, 409

def get_all():
    result = Products.query.all()
    try:
        Products.validate_id(result)
    except NotFoundError as e:
        return { "alert": "informações não encontradas" }, 404
    return jsonify(result), 200


def delete_products(id):
    current = Products.query.get(id)
    try:
        Products.validate_id(current)
    except NotFoundError as e:
        return e.message, 404
    current_app.db.session.delete(current)
    current_app.db.session.commit()
    return "", 204

    



