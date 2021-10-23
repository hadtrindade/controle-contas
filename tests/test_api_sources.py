from flask import url_for


def test_para_inserir_sources_de_teste(client, token):
    data = {
        "id": 1,
        "description": "teste",
        "id_user": 1,
    }
    response = client.post(
        url_for("api.new_sources"), json=data, headers=token
    )
    assert response.json == data


def test_para_inserir_lista_de_sources(client, token):
    data = [
        {
            "id": 2,
            "description": "test_de_moi",
            "id_user": 20,
        },
        {
            "id": 3,
            "description": "teste_test_de_moi",
            "id_user": 21,
        },
    ]
    response = client.post(
        url_for("api.new_sources"), json=data, headers=token
    )
    assert response.json == data


def test_para_consultar_sources_deve_retornar_status_code_200(client, token):
    respose = client.get(url_for("api.get_sources"), headers=token)
    assert respose.status_code == 200


def test_com_payload_invalido_deve_retornar_status_code_422(client, token):
    data = {
        "description": 1,
        "id_user": "a",
    }
    response = client.post(
        url_for("api.new_sources"), json=data, headers=token
    )
    assert response.status_code == 422


def test_cosultar_um_unico_source(client, token):
    data = {
        "id": 1,
        "description": "teste",
        "id_user": 1,
    }
    response = client.get(url_for("api.update_source", pk=1), headers=token)
    assert response.json[0] == data


def test_update_source(client, token):
    data = {
        "id": 1,
        "description": "teste_update",
        "id_user": 1,
    }
    response = client.put(
        url_for("api.update_source", pk=1), json=data, headers=token
    )
    assert response.status_code == 200


def test_update_de_source_deve_falhar_status_code_404(client, token):
    data = {
        "id": 1,
        "description": "teste_update",
        "id_user": 1,
    }
    response = client.put(
        url_for("api.update_source", pk=10), json=data, headers=token
    )
    assert response.status_code == 404


def test_delete_source_deve_retornar_200(client, token):

    response = client.delete(url_for("api.del_source", pk=1), headers=token)
    assert response.status_code == 200


def test_delete_source_deve_retornar_404(client, token):

    response = client.delete(url_for("api.del_source", pk=10), headers=token)
    assert response.status_code == 404
