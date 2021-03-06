from flask import Flask


def init_app(app: Flask):
    from app.routes.users_bluesprint import bp_users

    app.register_blueprint(bp_users)

    from app.routes.product_blueprint import bp_product

    app.register_blueprint(bp_product)


    from app.routes.products_user_blueprint import bp_list

    app.register_blueprint(bp_list)

    from app.routes.store_blueprint import bp_store

    app.register_blueprint(bp_store)