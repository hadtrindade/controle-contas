from flask import url_for


def test_consulta_deve_retornar_status_code_204_response_vazio(
    client,
):
    response = client.get(url_for("api_sources.get_sources"))
    assert response.status_code == 204


def test_para_inserir_sources_deve_retornar_status_code_201(client):
    data = {
        "id": 1,
        "description": "teste",
        "id_user": 1,
    }
    response = client.post(url_for("api_sources.new_sources"), json=data)
    assert response.json == data


def test_para_consultar_sources_deve_retornar_status_code_200(client):
    respose = client.get(url_for("api_sources.get_sources"))
    assert respose.status_code == 200


def test_com_payload_invalido_deve_retornar_status_code_422(client):
    data = {
        "description": 1,
        "id_user": "a",
    }
    response = client.post(url_for("api_sources.new_sources"), json=data)
    assert response.status_code == 422


def test_cosultar_um_unico_source(client):
    data = {
        "id": 1,
        "description": "teste",
        "id_user": 1,
    }
    response = client.get(url_for("api_sources.update_source", pk=1))
    assert response.json[0] == data


def test_update_source(client):
    data = {
        "id": 1,
        "description": "teste_update",
        "id_user": 1,
    }
    response = client.put(
        url_for("api_sources.update_source", pk=1, json=data)
    )
    assert response.status_code == 200


def test_update_de_source_deve_falhar_status_code_404(client):
    data = {
        "id": 1,
        "description": "teste_update",
        "id_user": 1,
    }
    response = client.put(
        url_for("api_sources.update_source", pk=10, json=data)
    )
    assert response.status_code == 404


def test_delete_source_deve_retornar_200(client):

    response = client.delete(url_for("api_sources.del_source", pk=1))
    assert response.status_code == 200


def test_delete_source_deve_retornar_404(client):

    response = client.delete(url_for("api_sources.del_source", pk=10))
    assert response.status_code == 404
