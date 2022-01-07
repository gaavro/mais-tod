from flask import Flask
from app.configs import commands, database, migration, env_configs, jwt_auth
from app import routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)


    env_configs.init_app(app)
    database.init_app(app)
    migration.init_app(app)    
    routes.init_app(app)
    jwt_auth.init_app(app)
    

    return app

