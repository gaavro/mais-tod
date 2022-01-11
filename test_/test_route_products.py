from flask.testing import FlaskClient
from flask_jwt_extended import create_access_token

from app import create_app

def test_route_products_exists(app_routes):
    assert app_routes.match("/product"), 'Verifique se existe uma rota "/product"'

def test_verify_is_get_all(client: FlaskClient):
    response = client.get("/product")      
    assert type(response.json) == dict




