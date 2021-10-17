from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
    set_access_cookies,
    unset_jwt_cookies,
)
from controle_contas.ext.auth.models import User
from controle_contas.ext.serializer.models import UserLoginSchema
from flask_marshmallow.sqla import ValidationError
from datetime import datetime, timedelta, timezone


auth = Blueprint("auth", __name__)


@auth.route("/api/v1/auth", methods=["POST"])
def get_token():
    try:
        user_login_schema = UserLoginSchema()
        data = user_login_schema.load(request.json)
    except ValidationError as err:
        return err.normalized_messages()
    user = User.query.filter_by(username=data["username"]).one_or_none()
    if not user or not user.check_password(data["password"]):
        return jsonify({"message": "Wrong username or password"}), 401
    access_token = create_access_token(identity=user.id, fresh=True)
    refresh_token = create_refresh_token(identity=user.id)
    return (
        jsonify(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "message": "success",
            }
        ),
        200,
    )


@auth.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response


@auth.route("/api/v1/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)


@auth.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        return response


def init_app(app):
    app.register_blueprint(auth)
