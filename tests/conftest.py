import pytest
from flask import url_for
from controle_contas.app import create_app
from controle_contas.ext.db import db
from werkzeug.security import generate_password_hash
from controle_contas.ext.serializer.models import UserSchema


@pytest.fixture(scope="session")
def app():
    app = create_app()
    app.testing = True
    app_context = app.test_request_context()
    app_context.push()
    app.db.create_all()

    data = {
        "username": "test",
        "first_name": "test",
        "last_name": "test",
        "email": "test@test.com",
        "password": generate_password_hash("123"),
        "admin": True,
    }
    user = UserSchema().load(data)

    db.session.add(user)
    db.session.commit()

    yield app
    app.db.drop_all()


@pytest.fixture()
def token(client):
    user = {"username": "test", "password": "123"}
    response = client.post(url_for("auth.get_token"), json=user)

    return {"Authorization": f'Bearer {response.json["access_token"]}'}
