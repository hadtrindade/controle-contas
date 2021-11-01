from flask_jwt_extended import JWTManager
from datetime import timedelta

jwt = JWTManager()


def init_app(app):

    jwt.init_app(app)
    app.config["JWT_TOKEN_LOCATION"] = ["cookies", "headers"]
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
