from flask.testing import FlaskClient
from flask_jwt_extended import create_access_token

def test_route_products_exists(app_routes):
    assert app_routes.match("/product"), 'Verifique se existe uma rota "/product"'




