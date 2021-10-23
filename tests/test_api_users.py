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
