from flask import Blueprint, current_app, request
from controle_contas.ext.serializer.models import (
    SourceSchema,
    UserSchema,
    EntrySchema,
)
from marshmallow import ValidationError
from controle_contas.ext.db.models import Source, Entry
from controle_contas.ext.auth.models import User


api = Blueprint("api", __name__)


@api.route("/api/v1/sources", methods=["GET"])
def get_sources():
    sources = Source.query.all()
    if not sources:
        return SourceSchema().jsonify(sources), 204
    return SourceSchema(many=True).jsonify(sources), 200


@api.route("/api/v1/sources", methods=["POST"])
def new_source():
    source_schema = SourceSchema()
    try:
        source = source_schema.loads(request.json)
    except ValidationError as err:
        return source_schema.jsonify(err.messages, many=True), 422
    s = Source(**source)
    current_app.db.session.add(s)
    current_app.db.session.commit()
    return source_schema.jsonify(source), 201


@api.route("/api/v1/users", methods=["GET"])
def get_users():
    users = User.query.all()
    if not users:
        return UserSchema().jsonify(users), 204
    return UserSchema(many=True).jsonify(users), 200


@api.route("/api/v1/users", methods=["POST"])
def new_user():

    user_schema = UserSchema()
    try:
        user = user_schema.loads(request.json)
    except ValidationError as err:
        return user_schema.jsonify(err.messages, many=True), 422
    u = User(**user)
    current_app.db.session.add(u)
    current_app.db.session.commit()
    return user_schema.jsonify(user), 201


@api.route("/api/v1/entry", methods=["GET"])
def get_entry():
    entry = Entry.query.all()
    if not entry:
        return EntrySchema().jsonify(entry), 204
    return EntrySchema(many=True).jsonify(entry), 200


@api.route("/api/v1/entry", methods=["POST"])
def new_entry():
    entry_schema = EntrySchema()
    try:
        entry = entry_schema.loads(request.json)
    except ValidationError as err:
        return entry_schema.jsonify(err.messages, many=True), 422
    e = Entry(**entry)
    current_app.db.session.add(e)
    current_app.db.session.commit()
    return entry_schema.jsonify(entry), 201
