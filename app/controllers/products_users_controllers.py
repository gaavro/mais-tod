from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.products_model import Products
from flask import current_app, jsonify, request
from app.models.customer_model import Customer
from app.models.products_user_model import ProductsUser


def add_to_list(id):
    data = request.get_json()    
    product= Products.query.filter_by(id= Products.id).first_or_404()
    result= product.value * data['qty']
    customer = Customer.query.filter_by(cpf=data['cpf']).first_or_404()
    list = ProductsUser(customer_id=customer.id, product_id= id, total= result)
    current_app.db.session.add(list)
    current_app.db.session.commit()    
    return jsonify(list), 200
