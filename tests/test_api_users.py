import json
import pytest
from flask import url_for


def test_para_get_users_deve_retornar_vazio_codigo_204(client):
    users = client.get(url_for("api.get_users"))
    assert users.status_code == 204


def test_para_inserir_usuários_deve_retornar_status_code_201(client):
    data = {
        "username": "teste",
        "email": "teste@test.com",
        "passwd": "1234",
        "admin": "true",
    }
    user = client.post(url_for("api.new_user"), json=json.dumps(data))
    assert user.status_code == 201


def test_para_get_users_deve_retornar_codigo_200(client):
    users = client.get(url_for("api.get_users"))
    assert users.status_code == 200


def test_para_inserir_usuários_com_payload_invalido_deve_retornar_status_code_422(
    client,
):
    data = {
        "username": 1,
        "email": "teste2test.com",
        "passwd": "1234",
        "admin": "a",
    }
    user = client.post(url_for("api.new_user"), json=json.dumps(data))
    assert user.status_code == 422
