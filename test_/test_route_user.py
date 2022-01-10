from app import create_app
from flask_jwt_extended import create_access_token

def test_create_user(client):
    url = "/register"
    data = {
	"name": "Gabriela",
	"email": "gabriela@email.com",
	"cpf": "12345678912",
	"password": "1234"
}
    expected = {
    "id": 1,
    "name": "Gabriela",
    "cpf": "12345678912",
    "email": "gabriela@email.com"
}
    res = client.post(url, json=data, headers={'Content-Type': 'application/json'})
    assert res.get_json() == expected


