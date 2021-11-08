from flask import url_for


def test_para_inserir_usuários_deve_retornar_status_code_201(client, token):
    data = {
        "username": "teste",
        "first_name": "teste",
        "last_name": "teste",
        "email": "teste@test.com",
        "password": "1234",
        "admin": "true",
    }
    response = client.post(url_for("api.new_users"), json=data, headers=token)
    assert response.status_code == 201


def test_para_inserir_lista_de_usuarios(client, token):
    data = [
        {
            "username": "teste_2",
            "first_name": "teste",
            "last_name": "teste",
            "email": "teste_2@test.com",
            "password": "1234",
            "admin": "false",
        },
        {
            "username": "teste_3",
            "first_name": "teste",
            "last_name": "teste",
            "email": "teste_3@test.com",
            "password": "1234",
            "admin": "false",
        },
    ]
    response = client.post(url_for("api.new_users"), json=data, headers=token)
    assert response.status_code == 201


def test_para_get_users_deve_retornar_codigo_200(client, token):
    users = client.get(url_for("api.get_users"), headers=token)
    assert users.status_code == 200


def test_para_inserir_com_payload_invalido_deve_retornar_status_code_422(
    client, token
):
    data = {
        "username": 1,
        "first_name": "teste",
        "last_name": "teste",
        "email": "teste2test.com",
        "password": "1234",
        "admin": "a",
    }
    user = client.post(url_for("api.new_users"), json=data, headers=token)
    assert user.status_code == 422


def test_cosultar_uma_unica_users(client, token):
    response = client.get(url_for("api.get_user", pk=2), headers=token)
    assert response.status_code == 200


def test_update_user(client, token):
    data = {
        "username": "teste_update",
        "first_name": "teste",
        "last_name": "teste",
        "email": "teste1@test.com",
        "password": "12343",
        "admin": "false",
    }
    response = client.put(
        url_for("api.update_user", pk=2), json=data, headers=token
    )
    assert response.status_code == 200


def test_update_de_users_deve_falhar_status_code_404(client, token):
    data = {
        "username": "teste",
        "first_name": "teste",
        "last_name": "teste",
        "email": "teste@test.com",
        "password": "1234",
        "admin": "true",
    }
    response = client.put(
        url_for("api.update_user", pk=10), json=data, headers=token
    )
    assert response.status_code == 404


def test_delete_users_deve_retornar_200(client, token):

    response = client.delete(url_for("api.del_user", pk=2), headers=token)
    assert response.status_code == 200


def test_delete_users_deve_retornar_404(client, token):

    response = client.delete(url_for("api.del_user", pk=10), headers=token)
    assert response.status_code == 404


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
            "id_user": 1,
        },
        {
            "id": 3,
            "description": "teste_test_de_moi",
            "id_user": 1,
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
        "id_user": 1,
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
            "id_source": 1,
            "id_user": 1,
            "revenue": "true",
        },
        {
            "description": "teste1",
            "value": 105,
            "quantum": 12,
            "id_source": 1,
            "id_user": 1,
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
        "id_user": 1,
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
        "id_user": 1,
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
        "id_user": 1,
        "revenue": "true",
    }
    response = client.put(
        url_for("api.update_entry", pk=10), json=data, headers=token
    )
    assert response.status_code == 404


def test_delete_entries_deve_retornar_200(client, token):

    response = client.delete(url_for("api.del_entry", pk=1), headers=token)
    assert response.status_code == 200


def test_delete_2_entries_deve_retornar_200(client, token):

    response = client.delete(url_for("api.del_entry", pk=2), headers=token)
    assert response.status_code == 200


def test_delete_3_entries_deve_retornar_200(client, token):

    response = client.delete(url_for("api.del_entry", pk=3), headers=token)
    assert response.status_code == 200


def test_delete_source_deve_retornar_404(client, token):

    response = client.delete(url_for("api.del_entry", pk=10), headers=token)
    assert response.status_code == 404


def test_delete_source_deve_retornar_200(client, token):

    response = client.delete(url_for("api.del_source", pk=1), headers=token)
    assert response.status_code == 200


def test_delete_source_deve_retornar_404(client, token):

    response = client.delete(url_for("api.del_source", pk=10), headers=token)
    assert response.status_code == 404
