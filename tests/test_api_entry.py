from flask import url_for


def test_para_consultar_entry_deve_retornar_status_code_204_porque_esta_vazio(
    client, token
):

    response = client.get(url_for("api.get_entries"), headers=token)
    assert response.status_code == 204


def test_para_inserir_entry_de_testes(client, token):
    data = {
        "description": "teste",
        "value": 10,
        "quantum": 1,
        "id_source": 1,
        "revenue": "true",
    }
    response = client.post(
        url_for("api.new_entries"), json=data, headers=token
    )
    assert response.status_code == 201


def test_para_inserir_lista_entries(client, token):
    data = [
        {
            "description": "teste1",
            "value": 102,
            "quantum": 13,
            "id_source": 14,
            "revenue": "true",
        },
        {
            "description": "teste1",
            "value": 105,
            "quantum": 12,
            "id_source": 13,
            "revenue": "false",
        },
    ]
    response = client.post(
        url_for("api.new_entries"), json=data, headers=token
    )
    assert response.status_code == 201


def test_para_consultar_sources_deve_retornar_status_code_200(client, token):
    response = client.get(url_for("api.get_entries"), headers=token)
    assert response.status_code == 200


def test_com_payload_invalido_não_deve_adicionar_uma_entries(client, token):
    data = {
        "description": 30,
        "value": "a",
        "quantum": 1,
        "id_source": 1,
        "revenue": "true",
    }
    response = client.post(
        url_for("api.new_entries"), json=data, headers=token
    )
    assert response.status_code == 422


def test_cosultar_uma_unica_entries(client, token):
    response = client.get(url_for("api.get_entry", pk=1), headers=token)
    assert response.status_code == 200


def test_update_entry(client, token):
    data = {
        "description": "teste_update",
        "value": 10,
        "quantum": 1,
        "id_source": 1,
        "revenue": "true",
    }
    response = client.put(
        url_for("api.update_entry", pk=1), json=data, headers=token
    )
    assert response.status_code == 200


def test_update_de_entries_deve_falhar_status_code_404(client, token):
    data = {
        "description": "teste",
        "value": 10,
        "quantum": 1,
        "id_source": 1,
        "revenue": "true",
    }
    response = client.put(
        url_for("api.update_entry", pk=10), json=data, headers=token
    )
    assert response.status_code == 404


def test_delete_entries_deve_retornar_200(client, token):

    response = client.delete(url_for("api.del_entry", pk=1), headers=token)
    assert response.status_code == 200


def test_delete_source_deve_retornar_404(client, token):

    response = client.delete(url_for("api.del_entry", pk=10), headers=token)
    assert response.status_code == 404
