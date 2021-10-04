from flask import Flask
from controle_contas.db import init_app as config_db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///controle_contas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)

    from controle_contas.auth.views import admin
    app.register_blueprint(admin)
    return app