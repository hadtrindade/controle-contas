from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from decouple import config

db = SQLAlchemy()
migrade = Migrate()

if config("FLASK_DEBUG", default=False):
    DATABASE_URI = config("DATABASE_URL_SQLITE", default="sqlite:///controle_contas.db")
else:
    DATABASE_URI = config("DATABASE_URL").replace("://", "ql://", 1)


def init_app(app):

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    app.db = db
    migrade.init_app(app, db)
