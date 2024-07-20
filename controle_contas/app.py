from os import getenv

from flask import Flask

from controle_contas.ext import admin, cli, db, jwt, login, serializer
from controle_contas.ext.api import views as v_api
from controle_contas.ext.auth import views as v_auth
from controle_contas.ext.site import views as v_site


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = getenv("SECRET_KEY")

    db.init_app(app)
    serializer.init_app(app)
    jwt.init_app(app)
    login.init_app(app)
    cli.init_app(app)
    admin.init_app(app)
    v_api.init_app(app)
    v_auth.init_app(app)
    v_site.init_app(app)

    return app
