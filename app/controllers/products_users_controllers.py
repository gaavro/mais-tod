from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.products_model import Products
from flask import current_app, jsonify, request
from app.models.products_user_model import ProductsUser
from app.exceptions.exceptions import UniqueUserError, InvalidTypeError, InvalidKeyError, NotFoundError
from app.models.users_model import Users
import requests

@jwt_required()
def add_to_list(id):
    try:
        order= request.get_json() 
        current = get_jwt_identity() 
        Products.validate_id(id)  
        product= Products.query.filter_by(id= Products.id).first_or_404()
        result= product.value * order['qty']
        discount= result * 0.2
        data= {"users_id": current["id"], "total":result, "product_id": id, "cashback":discount}
        
        url = "https://5efb30ac80d8170016f7613d.mockapi.io/api/mock/Cashback"        
        list = ProductsUser(**data)
       
        new_data = requests.post(url, data)
        current_app.db.session.add(list)
        current_app.db.session.commit()    
        return jsonify({
            "sold_at": list.sold_at,
            "customer": list.users,
            "total": list.total,
            "cashback": list.cashback,
            "products": [{
                "type": list.products,
                "qty": list.qty
            }]}) , 200            
    except UniqueUserError:
        return {"alerta": "CPF já cadastrado."}, 409
    except InvalidTypeError:
        return {"alerta": "Informações inválidas."}, 400
    except InvalidKeyError:
        return {
            "alerta": "Informações incorretas."
        }, 400
    except NotFoundError:
        return{"alerta": "Produto não encontrado"}, 400


@jwt_required()
def remove_from_list(id):
    current = get_jwt_identity()
    try:
        removed = ProductsUser.query.filter_by(product_id=id, users_id=current["id"]).first()

        current_app.db.session.delete(removed)
        current_app.db.session.commit()

        return "", 204
    except NotFoundError:
        return {"alerta": "Usuário não encontrada"}, 404






        