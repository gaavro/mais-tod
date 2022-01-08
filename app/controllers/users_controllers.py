from flask import request, current_app, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.exceptions.exceptions import (
    InvalidKeyError,
    InvalidTypeError,
    NotFoundError,
    UniqueUserError,
)
from app.models.users_model import Users


def create_user():
    try:
        data = request.get_json()
        Users.validate_register_args(data)
        user = Users(**data)
        current_app.db.session.add(user)
        current_app.db.session.commit()
       
        return jsonify(user), 201
    except UniqueUserError:
        return {"alerta": "E-mail já cadastrado."}, 409
    except InvalidTypeError:
        return {"alerta": "Informações inválidas (apenas texto)."}, 400
    except InvalidKeyError:
        return {
            "alerta": "Informações incorretas (nome, e-mail)."
        }, 400


def login_user():
    try:
        data = request.json
        Users.validate_login_args(data)
        user = Users.query.filter_by(email=data["email"]).first()
        if not user:
            raise NotFoundError
        if user.validate_password(data["password"]):
            token = create_access_token(user)
            return {"token": token}, 200
    except NotFoundError:
        return {"alerta": "Usuário não encontrado"}, 404
    except InvalidKeyError:
        return {"alerta": "Informações incorretas (e-mail e senha)."}, 400
    except InvalidTypeError:
        return {"alerta": "Informações inválidas (apenas texto)."}, 400


def get_user():
    result = Users.query.all()
    if len(result) == 0:
        return {"alerta": "Nenhum dado encontrado"}, 404
    return jsonify(result), 200
    


@jwt_required()
def delete_users():
    current = get_jwt_identity()
    try:
        user = Users.query.get(current["id"])
        if user is None:
            raise NotFoundError
        current_app.db.session.delete(user)
        current_app.db.session.commit()
        return "", 204
    except NotFoundError:
        return {"alerta": "Usuário não encontrada"}, 404


@jwt_required()
def change_users():
    current = get_jwt_identity()
    try:
        user = Users.query.get(current["id"])
        data = request.json
        Users.validate_patch_args(data)

        if not user:
            raise NotFoundError

        for key, value in data.items():
            setattr(user, key, value)

        current_app.db.session.add(user)
        current_app.db.session.commit()

        return jsonify(user), 200

    except NotFoundError:
        return {"alerta": "Usuário não encontrada"}, 404
    except InvalidTypeError:
        return {"alerta": "Informações inválidas (apenas texto)."}, 400
    except InvalidKeyError:
        return {
            "alerta": "Informações incorretas (nome, e-mail, ou senha)."
        }, 400
