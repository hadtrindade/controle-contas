from flask import url_for


def test_deve_gerar_um_token(client):
    user = {"username": "test", "password": "123"}
    esperado = ["access_token", "message", "refresh_token"]
    response = client.post(url_for("auth.get_token"), json=user)
    assert list(response.json.keys()) == esperado


def test_deve_falhar_ao_gerar_um_token(client):
    user = {"username": "test", "password": "12323"}
    esperado = "Wrong username or password"
    response = client.post(url_for("auth.get_token"), json=user)
    assert response.json['message'] == esperado
