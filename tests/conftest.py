import pytest
from controle_contas.app import create_app


@pytest.fixture(scope="module")
def app():
    app = create_app()
    app.testing = True
    app_context = app.test_request_context()
    app_context.push()
    app.db.create_all()

    yield app
    app.db.drop_all()
