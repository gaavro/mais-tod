from flask import Blueprint
from app.controllers.costumers_controllers import get_all, delete_customer, create_customer


bp_customer = Blueprint("bp_customer", __name__)

bp_customer.post("/customer")(create_customer)
bp_customer.get("/customer")(get_all)
bp_customer.delete("/customer/<id>")(delete_customer)
