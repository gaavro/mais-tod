from flask import Blueprint
from app.controllers.store_controllers import get_store, delete_users, create_store, change_users, login_store


bp_store = Blueprint("bp_store", __name__)

bp_store.post("/store_cadastro")(create_store)
bp_store.post("/store")(login_store)
bp_store.get("/store")(get_store)
bp_store.patch("/store")(change_users)
bp_store.delete("/store")(delete_users)