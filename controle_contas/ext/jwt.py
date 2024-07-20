from datetime import timedelta
from os import getenv

from flask_jwt_extended import JWTManager

jwt = JWTManager()


def init_app(app):

    jwt.init_app(app)
    app.config["JWT_SECRET_KEY"] = getenv("JWT_SECRET_KEY", "test")
    app.config["JWT_TOKEN_LOCATION"] = ["cookies", "headers"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
