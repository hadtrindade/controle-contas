import pytest
from flask import url_for
from controle_contas.app import create_app
from controle_contas.ext.db import db
from werkzeug.security import generate_password_hash
from controle_contas.ext.auth.models import User
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
    data_is_valid = UserSchema().load(data)
    user = [User(**data_is_valid)]
    db.session.bulk_save_objects(user)
    db.session.commit()

    yield app
    app.db.drop_all()


@pytest.fixture(scope="function")
def token(client):
    user = {"username": "test", "password": "123"}
    response = client.post(url_for("auth.get_token"), json=user)

    return {"Authorization": "Bearer " + response.json["access_token"]}
