import json
from flask import url_for


def test_para_consultar_entry_deve_retornar_status_code_204_porque_esta_vazio(
    client,
):
    sources = client.get(url_for("api.get_entry"))
    assert sources.status_code == 204


def test_para_inserir_entry_deve_retornar_status_code_201(client):
    data = {
        "description": "teste",
        "value": 10,
        "quantum": 1,
        "id_source": 1,
        "revenue": "true",
    }
    user = client.post(url_for("api.new_entry"), json=json.dumps(data))
    assert user.status_code == 201


def test_para_consultar_sources_deve_retornar_status_code_200(client):
    entry = client.get(url_for("api.get_entry"))
    assert entry.status_code == 200


def test_com_payload_invalido_deve_retornar_status_code_422(client):
    data = {
        "description": 30,
        "value": "a",
        "quantum": 1,
        "id_source": 1,
        "revenue": "true",
    }
    user = client.post(url_for("api.new_entry"), json=json.dumps(data))
    assert user.status_code == 422