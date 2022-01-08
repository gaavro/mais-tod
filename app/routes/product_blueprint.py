from flask import Blueprint
from app.controllers.product_controllers import delete_products, register_products, get_all


bp_product = Blueprint("bp_product", __name__)

bp_product.post("/product")(register_products)
bp_product.get("/product")(get_all)
bp_product.delete("/product/<id>")(delete_products)
