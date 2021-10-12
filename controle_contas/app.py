from flask import Flask
from controle_contas.ext import db
from controle_contas.ext import serializer
from controle_contas.ext.db import models  # noqa
from controle_contas.ext.auth import models  # noqa


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///controle_contas.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    serializer.init_app(app)

    from controle_contas.ext.auth.views import admin

    app.register_blueprint(admin)

    from controle_contas.ext.api.views import api

    app.register_blueprint(api)

    return app
