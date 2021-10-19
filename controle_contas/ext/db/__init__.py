from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from os import getenv

db = SQLAlchemy()
migrade = Migrate()


def init_app(app):

    if not app.config["DEBUG"]:

        app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace(
            "://", "ql://", 1
        )
    db.init_app(app)
    app.db = db
    migrade.init_app(app, db)
