from os import getenv

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrade = Migrate()


def init_app(app):

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
    db.init_app(app)
    app.db = db
    migrade.init_app(app, db)
