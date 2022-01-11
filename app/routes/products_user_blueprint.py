from flask import Blueprint
from app.controllers.products_users_controllers import add_to_list, remove_from_list
bp_list = Blueprint("bp_list", __name__)

bp_list.post("/list/<id>")(add_to_list)
bp_list.delete("/list/<id>")(remove_from_list)


