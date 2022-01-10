def test_create_store(client):
    url = "/store_cadastro"
    data = {
	"name": "Gabriela",
	"cnpj": "12345678912",
	"password": "1234"
    }
    expected = {
    "name": "Gabriela",
    "id":1,
	"cnpj": "12345678912" 
       
    }
    res = client.post(url, json=data, headers={'Content-Type': 'application/json'})
    assert res.get_json() == expected