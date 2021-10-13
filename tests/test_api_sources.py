import json
from flask import url_for


def test_para_consultar_sources_deve_retornar_status_code_204_porque_esta_vazio(
    client,
):
    sources = client.get(url_for("api.get_sources"))
    assert sources.status_code == 204


def test_para_inserir_sources_deve_retornar_status_code_201(client):
    data = {
        "description": "teste",
        "id_user": 1,
    }
    user = client.post(url_for("api.new_source"), json=json.dumps(data))
    assert user.status_code == 201


def test_para_consultar_sources_deve_retornar_status_code_200(client):
    sources = client.get(url_for("api.get_sources"))
    assert sources.status_code == 200


def test_com_payload_invalido_deve_retornar_status_code_422(client):
    data = {
        "description": 1,
        "id_user": "a",
    }
    user = client.post(url_for("api.new_source"), json=json.dumps(data))
    assert user.status_code == 422
