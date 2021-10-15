from flask import url_for


def test_para_consultar_entry_deve_retornar_status_code_204_porque_esta_vazio(
    client,
):
    response = client.get(url_for("api_entries.get_entries"))
    assert response.status_code == 204


def test_para_inserir_entry_deve_retornar_status_code_201(client):
    data = {
        "description": "teste",
        "value": 10,
        "quantum": 1,
        "id_source": 1,
        "revenue": "true",
    }
    response = client.post(url_for("api_entries.new_entries"), json=data)
    assert response.status_code == 201


def test_para_consultar_sources_deve_retornar_status_code_200(client):
    response = client.get(url_for("api_entries.get_entries"))
    assert response.status_code == 200


def test_com_payload_invalido_deve_retornar_status_code_422(client):
    data = {
        "description": 30,
        "value": "a",
        "quantum": 1,
        "id_source": 1,
        "revenue": "true",
    }
    response = client.post(url_for("api_entries.new_entries"), json=data)
    assert response.status_code == 422


def test_cosultar_uma_unica_entries(client):
    response = client.get(url_for("api_entries.get_entry", pk=1))
    assert response.status_code == 200


def test_update_entry(client):
    data = {
        "description": "teste_update",
        "value": 10,
        "quantum": 1,
        "id_source": 1,
        "revenue": "true",
    }
    response = client.put(
        url_for("api_entries.update_entry", pk=1, json=data)
    )
    assert response.status_code == 200


def test_update_de_entries_deve_falhar_status_code_404(client):
    data = {
        "description": "teste",
        "value": 10,
        "quantum": 1,
        "id_source": 1,
        "revenue": "true",
    }
    response = client.put(
        url_for("api_entries.update_entry", pk=10, json=data)
    )
    assert response.status_code == 404


def test_delete_entries_deve_retornar_200(client):

    response = client.delete(url_for("api_entries.del_entry", pk=1))
    assert response.status_code == 200


def test_delete_source_deve_retornar_404(client):

    response = client.delete(url_for("api_entries.del_entry", pk=10))
    assert response.status_code == 404
