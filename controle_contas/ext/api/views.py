from flask import Blueprint, current_app, request
from flask_jwt_extended import current_user, jwt_required
from marshmallow import ValidationError

from controle_contas.ext.auth.models import User
from controle_contas.ext.db.models import Entry, Source
from controle_contas.ext.jwt import jwt
from controle_contas.ext.serializer.models import (
    EntrySchema,
    SourceSchema,
    UserSchema,
)

api = Blueprint("api", __name__)


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()


@api.route("/api/v1/entries", methods=["GET"])
@jwt_required()
def get_entries():
    entry = Entry.query.filter_by(id_user=current_user.id).all()
    if not entry:
        return EntrySchema().jsonify(entry), 204
    return EntrySchema(many=True).jsonify(entry), 200


@api.route("/api/v1/entries/<int:pk>", methods=["GET"])
@jwt_required()
def get_entry(pk):
    query = Entry.query.filter_by(id_user=current_user.id, id=pk).one_or_none()
    if not query:
        return EntrySchema().jsonify({"msg": "not found"}), 404
    return EntrySchema().jsonify(query), 200


@api.route("/api/v1/entries/<int:pk>", methods=["DELETE"])
@jwt_required()
def del_entry(pk):
    query = Entry.query.filter_by(id_user=current_user.id, id=pk)
    if not query.first():
        return EntrySchema().jsonify({"msg": "not found"}), 404
    query.delete()
    current_app.db.session.commit()
    return EntrySchema().jsonify({"msg": "deleted"}), 200


@api.route("/api/v1/entries/<int:pk>", methods=["PUT"])
@jwt_required()
def update_entry(pk):
    entry_schema = EntrySchema(load_instance=False)
    query = Entry.query.filter_by(id_user=current_user.id, id=pk)
    if not query.first():
        return EntrySchema().jsonify({"msg": "not found"}), 404
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


# Sources


@api.route("/api/v1/sources", methods=["GET"])
@jwt_required()
def get_sources():
    query = Source.query.filter_by(id_user=current_user.id).all()
    if not query:
        return SourceSchema().jsonify(query), 204
    return SourceSchema(many=True).jsonify(query), 200


@api.route("/api/v1/sources/<int:pk>", methods=["GET"])
@jwt_required()
def get_source(pk):
    query = Source.query.filter_by(id_user=current_user.id, id=pk)
    if not query.first():
        return SourceSchema().jsonify({}), 204
    return SourceSchema(many=True).jsonify(query), 200


@api.route("/api/v1/sources/<int:pk>", methods=["DELETE"])
@jwt_required()
def del_source(pk):

    query = Source.query.filter_by(id_user=current_user.id, id=pk)
    if not query.first():
        return SourceSchema().jsonify({"msg": "not found"}), 404
    query.delete()
    current_app.db.session.commit()
    return SourceSchema(many=True).jsonify({"msg": "deleted"}), 200


@api.route("/api/v1/sources/<int:pk>", methods=["PUT"])
@jwt_required()
def update_source(pk):
    source_schema = SourceSchema(load_instance=False)
    query = Source.query.filter_by(id_user=current_user.id, id=pk)
    if not query.first():
        return source_schema.jsonify({"msg": "not found"}), 404
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
    query = User.query.with_entities(
        User.username, User.first_name, User.last_name
    ).all()
    if not query:
        return UserSchema().jsonify({}), 204
    return UserSchema(many=True).jsonify(query), 200


@api.route("/api/v1/users/<int:pk>", methods=["GET"])
@jwt_required()
def get_user(pk):

    query = (
        User.query.filter_by(id=pk)
        .with_entities(User.username, User.first_name, User.last_name)
        .one_or_none()
    )
    if not query:
        return UserSchema().jsonify({"msg": "not found"}), 404
    return UserSchema(many=True).jsonify(query), 200


@api.route("/api/v1/users/<int:pk>", methods=["DELETE"])
@jwt_required()
def del_user(pk):

    if current_user.is_staff:
        query = User.query.filter(User.id == pk)
        if not query.first():
            return UserSchema().jsonify({"msg": "not found"}), 404
        query.delete()
        current_app.db.session.commit()
        return UserSchema().jsonify({"msg": "deleted"}), 200
    return UserSchema().jsonify({"msg": "Forbidden"}), 403


@api.route("/api/v1/users/<int:pk>", methods=["PUT"])
@jwt_required()
def update_user(pk):
    if current_user.is_staff:
        user_schema = UserSchema(load_instance=False)
        query = User.query.filter(User.id == pk)

        if not query.first():
            return user_schema.jsonify({"msg": "not found"}), 404
        try:
            data = user_schema.load(request.json)
        except ValidationError as err:
            return err.normalized_messages(), 422
        query.update(data)
        current_app.db.session.commit()
        return user_schema.jsonify(data), 200
    return UserSchema().jsonify({"msg": "Forbidden"}), 403


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
