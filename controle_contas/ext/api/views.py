import ast
from flask import Blueprint, current_app, request
from controle_contas.ext.serializer.models import (
    EntrySchema,
    UserSchema,
    SourceSchema,
)
from marshmallow import ValidationError
from controle_contas.ext.db.models import Entry, Source

from controle_contas.ext.auth.models import User

api = Blueprint("api", __name__)


@api.route("/api/v1/entries", methods=["GET"])
def get_entries():
    entry = Entry.query.all()
    if not entry:
        return EntrySchema().jsonify(entry), 204
    return EntrySchema(many=True).jsonify(entry), 200


@api.route("/api/v1/entries/<int:pk>", methods=["GET"])
def get_entry(pk):
    query = Entry.query.filter(Entry.id == pk)
    if not query.first():
        return EntrySchema().jsonify({}), 404
    return EntrySchema(many=True).jsonify(query), 200


@api.route("/api/v1/entries/<int:pk>", methods=["DELETE"])
def del_entry(pk):
    query = Entry.query.filter(Entry.id == pk)
    if not query.first():
        return EntrySchema().jsonify({}), 404
    query.delete()
    current_app.db.session.commit()
    return EntrySchema(many=True).jsonify({}), 200


@api.route("/api/v1/entries/<int:pk>", methods=["PUT"])
def update_entry(pk):
    entry_schema = EntrySchema()
    query = Entry.query.filter(Entry.id == pk)
    if not query.first():
        return EntrySchema().jsonify({}), 404

    if not request.json:
        try:
            data = entry_schema.load(
                ast.literal_eval(request.args.to_dict()["json"])
            )
        except ValidationError as err:
            return err.normalized_messages(), 422
    else:
        try:
            data = entry_schema.load(request.json)
        except ValidationError as err:
            return err.normalized_messages(), 422
    query.update(data)
    current_app.db.session.commit()
    return EntrySchema(many=True).jsonify(query), 200


@api.route("/api/v1/entries", methods=["POST"])
def new_entries():
    entry_schema = EntrySchema()
    try:
        data = entry_schema.load(request.json)
    except ValidationError as err:
        return err.normalized_messages(), 422
    entry = Entry(**data)
    current_app.db.session.add(entry)
    current_app.db.session.commit()
    return entry_schema.jsonify(data), 201


@api.route("/api/v1/sources", methods=["GET"])
def get_sources():
    query = Source.query.all()
    if not query:
        return SourceSchema().jsonify(query), 204
    return SourceSchema(many=True).jsonify(query), 200


@api.route("/api/v1/sources/<int:pk>", methods=["GET"])
def get_source(pk):
    query = Source.query.filter(Source.id == pk)
    if not query.first():
        return SourceSchema().jsonify(query), 204
    return SourceSchema(many=True).jsonify(query), 200


@api.route("/api/v1/sources/<int:pk>", methods=["DELETE"])
def del_source(pk):

    query = Source.query.filter(Source.id == pk)
    if not query.first():
        return SourceSchema().jsonify({}), 404
    query.delete()
    current_app.db.session.commit()
    return SourceSchema(many=True).jsonify({}), 200


@api.route("/api/v1/sources/<int:pk>", methods=["PUT"])
def update_source(pk):
    source_schema = SourceSchema()
    query = Source.query.filter(Source.id == pk)
    if not query.first():
        return source_schema.jsonify({}), 404
    if not request.json:
        try:
            data = source_schema.load(
                ast.literal_eval(request.args.to_dict()["json"])
            )
        except ValidationError as err:
            return err.normalized_messages(), 422
    else:
        try:
            data = source_schema.load(request.json)
        except ValidationError as err:
            return err.normalized_messages(), 422
    query.update(data)
    current_app.db.session.commit()
    return SourceSchema().jsonify(query), 200


@api.route("/api/v1/sources", methods=["POST"])
def new_sources():
    source_schema = SourceSchema()
    try:
        data = source_schema.load(request.json)
    except ValidationError as err:
        return err.normalized_messages(), 422
    source = Source(**data)
    current_app.db.session.add(source)
    current_app.db.session.commit()
    return source_schema.jsonify(data), 201


@api.route("/api/v1/users", methods=["GET"])
def get_users():
    query = User.query.all()
    if not query:
        return UserSchema().jsonify(query), 204
    return UserSchema(many=True).jsonify(query), 200


@api.route("/api/v1/users/<int:pk>", methods=["GET"])
def get_user(pk):

    query = User.query.filter(User.id == pk)
    if not query.first():
        return UserSchema().jsonify({}), 404
    return UserSchema(many=True).jsonify(query), 200


@api.route("/api/v1/users/<int:pk>", methods=["DELETE"])
def del_user(pk):

    query = User.query.filter(User.id == pk)
    if not query.first():
        return UserSchema().jsonify({}), 404
    query.delete()
    current_app.db.session.commit()
    return UserSchema(many=True).jsonify({}), 200


@api.route("/api/v1/users/<int:pk>", methods=["PUT"])
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


@api.route("/api/v1/users", methods=["POST"])
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
