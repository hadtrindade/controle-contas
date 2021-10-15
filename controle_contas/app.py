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

    from controle_contas.ext.api.views_sources import api_sources

    app.register_blueprint(api_sources)

    from controle_contas.ext.api.views_users import api_users

    app.register_blueprint(api_users)

    from controle_contas.ext.api.views_entries import api_entries

    app.register_blueprint(api_entries)
    return app
