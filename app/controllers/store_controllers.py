from flask import request, current_app, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.exceptions.exceptions import (
    InvalidKeyError,
    InvalidTypeError,
    NotFoundError,
    UniqueUserError,
)
from app.models.users_model import Users
from app.models.store_model import Store


def create_store():
    try:
        data = request.get_json()
        Store.validate_register_args(data)
        store = Store(**data)    
        current_app.db.session.add(store)
        current_app.db.session.commit()
       
        return jsonify(store), 201
    except UniqueUserError:
        return {"alerta": "E-mail já cadastrado."}, 409
    except InvalidTypeError:
        return {"alerta": "Informações inválidas (apenas texto)."}, 400
    except InvalidKeyError:
        return {
            "alerta": "Informações incorretas (nome, e-mail)."
        }, 400


def login_store():
    try:
        data = request.json
        Store.validate_login_args(data)
        store = Store.query.filter_by(cnpj=data["cnpj"]).first()
        if not store:
            raise NotFoundError
        if store.validate_password(data["password"]):
            token = create_access_token(store)
            return {"token": token}, 200
    except NotFoundError:
        return {"alerta": "Usuário não encontrado"}, 404
    except InvalidKeyError:
        return {"alerta": "Informações incorretas (e-mail e senha)."}, 400
    except InvalidTypeError:
        return {"alerta": "Informações inválidas (apenas texto)."}, 400


def get_store():
    try:
        result = Store.query.all()
    except NotFoundError as e:
        return e.message, 404
    return jsonify(result), 200
    


@jwt_required()
def delete_users():
    current = get_jwt_identity()
    try:
        store = Store.query.get(current["id"])
        if store is None:
            raise NotFoundError
        current_app.db.session.delete(store)
        current_app.db.session.commit()
        return "", 204
    except NotFoundError:
        return {"alerta": "Usuário não encontrada"}, 404


@jwt_required()
def change_users():
    current = get_jwt_identity()
    try:
        store = Store.query.get(current["id"])
        data = request.json
        Store.validate_patch_args(data)

        if not store:
            raise NotFoundError

        for key, value in data.items():
            setattr(store, key, value)

        current_app.db.session.add(store)
        current_app.db.session.commit()

        return jsonify(store), 200

    except NotFoundError:
        return {"alerta": "Usuário não encontrada"}, 404
    except InvalidTypeError:
        return {"alerta": "Informações inválidas (apenas texto)."}, 400
    except InvalidKeyError:
        return {
            "alerta": "Informações incorretas (nome, e-mail, ou senha)."
        }, 400
