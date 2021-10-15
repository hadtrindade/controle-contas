import ast
from flask import Blueprint, current_app, request
from controle_contas.ext.serializer.models import (
    UserSchema,
)
from marshmallow import ValidationError
from controle_contas.ext.auth.models import User


api_users = Blueprint("api_users", __name__)


@api_users.route("/api/v1/users", methods=["GET"])
def get_users():
    query = User.query.all()
    if not query:
        return UserSchema().jsonify(query), 204
    return UserSchema(many=True).jsonify(query), 200


@api_users.route("/api/v1/users/<int:pk>", methods=["GET"])
def get_user(pk):

    query = User.query.filter(User.id == pk)
    if not query.first():
        return UserSchema().jsonify({}), 404
    return UserSchema(many=True).jsonify(query), 200


@api_users.route("/api/v1/users/<int:pk>", methods=["DELETE"])
def del_user(pk):

    query = User.query.filter(User.id == pk)
    if not query.first():
        return UserSchema().jsonify({}), 404
    query.delete()
    current_app.db.session.commit()
    return UserSchema(many=True).jsonify({}), 200


@api_users.route("/api/v1/users/<int:pk>", methods=["PUT"])
def update_user(pk):
    user_schema = UserSchema()
    query = User.query.filter(User.id == pk)

    if not query.first():
        return user_schema.jsonify({}), 404
    if not request.json:
        try:
            data = user_schema.load(
                ast.literal_eval(request.args.to_dict()["json"])
            )
        except ValidationError as err:
            return err.normalized_messages(), 422
    else:
        try:
            data = user_schema.load(request.json)
        except ValidationError as err:
            return err.normalized_messages(), 422
    user = User(**data)
    current_app.db.session.add(user)
    current_app.db.session.commit()
    return user_schema.jsonify(data), 200


@api_users.route("/api/v1/users", methods=["POST"])
def new_users():

    user_schema = UserSchema()
    try:
        data = user_schema.load(request.json)
    except ValidationError as err:
        return err.normalized_messages(), 422
    user = User(**data)
    current_app.db.session.add(user)
    current_app.db.session.commit()
    return user_schema.jsonify(data), 201
