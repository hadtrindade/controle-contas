from flask import Blueprint, current_app, request
from controle_contas.ext.serializer.models import (
    EntrySchema,
    UserSchema,
    SourceSchema,
)
from marshmallow import ValidationError
from controle_contas.ext.db.models import Entry, Source
from controle_contas.ext.auth.models import User
from flask_jwt_extended import jwt_required


api = Blueprint("api", __name__)


@api.route("/api/v1/entries", methods=["GET"])
@jwt_required()
def get_entries():
    entry = Entry.query.all()
    if not entry:
        return EntrySchema().jsonify(entry), 204
    return EntrySchema(many=True).jsonify(entry), 200


@api.route("/api/v1/entries/<int:pk>", methods=["GET"])
@jwt_required()
def get_entry(pk):
    query = Entry.query.filter(Entry.id == pk)
    if not query.first():
        return EntrySchema().jsonify({}), 404
    return EntrySchema(many=True).jsonify(query), 200


@api.route("/api/v1/entries/<int:pk>", methods=["DELETE"])
@jwt_required()
def del_entry(pk):
    query = Entry.query.filter(Entry.id == pk)
    if not query.first():
        return EntrySchema().jsonify({}), 404
    query.delete()
    current_app.db.session.commit()
    return EntrySchema(many=True).jsonify({"message": "excluido"}), 200


@api.route("/api/v1/entries/<int:pk>", methods=["PUT"])
@jwt_required()
def update_entry(pk):
    entry_schema = EntrySchema(load_instance=False)
    query = Entry.query.filter(Entry.id == pk)
    if not query.first():
        return EntrySchema().jsonify({}), 404
    try:
        data = entry_schema.load(request.json)
    except ValidationError as err:
        return err.normalized_messages(), 422
    query.update(data)
    current_app.db.session.commit()
    return EntrySchema(many=True).jsonify(query), 200


@api.route("/api/v1/entries", methods=["POST"])
@jwt_required()
def new_entries():
    entry_schema = EntrySchema()
    try:
        if isinstance(request.json, list):
            entries = entry_schema.load(
                request.json, many=True, session=current_app.db.session
            )
            current_app.db.session.add_all(entries)
            current_app.db.session.commit()
            return entry_schema.jsonify(entries, many=True), 201
        else:
            entry = entry_schema.load(
                request.json, session=current_app.db.session
            )
            current_app.db.session.add(entry)
            current_app.db.session.commit()
            return entry_schema.jsonify(entry), 201
    except ValidationError as err:
        return err.normalized_messages(), 422


@api.route("/api/v1/sources", methods=["GET"])
@jwt_required()
def get_sources():
    query = Source.query.all()
    if not query:
        return SourceSchema().jsonify(query), 204
    return SourceSchema(many=True).jsonify(query), 200


@api.route("/api/v1/sources/<int:pk>", methods=["GET"])
@jwt_required()
def get_source(pk):
    query = Source.query.filter(Source.id == pk)
    if not query.first():
        return SourceSchema().jsonify(query), 204
    return SourceSchema(many=True).jsonify(query), 200


@api.route("/api/v1/sources/<int:pk>", methods=["DELETE"])
@jwt_required()
def del_source(pk):

    query = Source.query.filter(Source.id == pk)
    if not query.first():
        return SourceSchema().jsonify({}), 404
    query.delete()
    current_app.db.session.commit()
    return SourceSchema(many=True).jsonify({}), 200


@api.route("/api/v1/sources/<int:pk>", methods=["PUT"])
@jwt_required()
def update_source(pk):
    source_schema = SourceSchema(load_instance=False)
    query = Source.query.filter(Source.id == pk)
    if not query.first():
        return source_schema.jsonify({}), 404
    try:
        data = source_schema.load(request.json)
    except ValidationError as err:
        return err.normalized_messages(), 422
    query.update(data)
    current_app.db.session.commit()
    return SourceSchema().jsonify(query), 200


@api.route("/api/v1/sources", methods=["POST"])
@jwt_required()
def new_sources():
    source_schema = SourceSchema()
    try:
        if isinstance(request.json, list):
            sources = source_schema.load(
                request.json, many=True, session=current_app.db.session
            )
            current_app.db.session.add_all(sources)
            current_app.db.session.commit()
            return source_schema.jsonify(sources, many=True), 201
        else:
            source = source_schema.load(
                request.json, session=current_app.db.session
            )
            current_app.db.session.add(source)
            current_app.db.session.commit()
            return source_schema.jsonify(source), 201
    except ValidationError as err:
        return err.normalized_messages(), 422


@api.route("/api/v1/users", methods=["GET"])
@jwt_required()
def get_users():
    query = User.query.all()
    if not query:
        return UserSchema().jsonify(query), 204
    return UserSchema(many=True).jsonify(query), 200


@api.route("/api/v1/users/<int:pk>", methods=["GET"])
@jwt_required()
def get_user(pk):

    query = User.query.filter(User.id == pk)
    if not query.first():
        return UserSchema().jsonify({}), 404
    return UserSchema(many=True).jsonify(query), 200


@api.route("/api/v1/users/<int:pk>", methods=["DELETE"])
@jwt_required()
def del_user(pk):

    query = User.query.filter(User.id == pk)
    if not query.first():
        return UserSchema().jsonify({}), 404
    query.delete()
    current_app.db.session.commit()
    return UserSchema(many=True).jsonify({}), 200


@api.route("/api/v1/users/<int:pk>", methods=["PUT"])
@jwt_required()
def update_user(pk):
    user_schema = UserSchema(load_instance=False)
    query = User.query.filter(User.id == pk)

    if not query.first():
        return user_schema.jsonify({}), 404
    try:
        data = user_schema.load(request.json)
    except ValidationError as err:
        return err.normalized_messages(), 422
    query.update(data)
    current_app.db.session.commit()
    return user_schema.jsonify(data), 200


@api.route("/api/v1/users", methods=["POST"])
@jwt_required()
def new_users():

    user_schema = UserSchema()
    try:
        if isinstance(request.json, list):
            users = user_schema.load(
                request.json, many=True, session=current_app.db.session
            )
            current_app.db.session.add_all(users)
            current_app.db.session.commit()
            return user_schema.jsonify(users, many=True), 201
        else:
            user = user_schema.load(
                request.json, session=current_app.db.session
            )
            current_app.db.session.add(user)
            current_app.db.session.commit()
            return user_schema.jsonify(user), 201
    except ValidationError as err:
        return err.normalized_messages(), 422


def init_app(app):
    app.register_blueprint(api)
