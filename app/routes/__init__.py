from flask import Flask


def init_app(app: Flask):
    from app.routes.users_bluesprint import bp_users

    app.register_blueprint(bp_users)
