from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)

    app.db = db

    from app.models.users_model import Users
    from app.models.products_model import Products
    from app.models.products_user_model import ProductsUser
    from app.models.store_model import Store