from flask import Flask
from controle_contas.ext import db
from controle_contas.ext import serializer
from controle_contas.ext.db import models  # noqa
from controle_contas.ext.auth import models  # noqa
from controle_contas.ext import babel
from controle_contas.ext import login
from controle_contas.ext.admin import admin
from controle_contas.ext import cli


def create_app():
    app = Flask(__name__)
    app.secret_key = "senhafacilquevaiparavardeambiente"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///controle_contas.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["BABEL_DEFAULT_LOCALE"] = "pt"
    babel.init_app(app)
    db.init_app(app)
    serializer.init_app(app)
    login.init_app(app)
    admin.init_app(app)
    cli.init_app(app)

    from controle_contas.ext.auth import views

    app.register_blueprint(views.auth)

    from controle_contas.ext.api import views

    app.register_blueprint(views.api)
    return app
