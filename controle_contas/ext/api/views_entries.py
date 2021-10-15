import ast
from flask import Blueprint, current_app, request
from controle_contas.ext.serializer.models import (
    EntrySchema,
)
from marshmallow import ValidationError
from controle_contas.ext.db.models import Entry


api_entries = Blueprint("api_entries", __name__)


@api_entries.route("/api/v1/entries", methods=["GET"])
def get_entries():
    entry = Entry.query.all()
    if not entry:
        return EntrySchema().jsonify(entry), 204
    return EntrySchema(many=True).jsonify(entry), 200


@api_entries.route("/api/v1/entries/<int:pk>", methods=["GET"])
def get_entry(pk):
    query = Entry.query.filter(Entry.id == pk)
    if not query.first():
        return EntrySchema().jsonify({}), 404
    return EntrySchema(many=True).jsonify(query), 200


@api_entries.route("/api/v1/entries/<int:pk>", methods=["DELETE"])
def del_entry(pk):
    query = Entry.query.filter(Entry.id == pk)
    if not query.first():
        return EntrySchema().jsonify({}), 404
    query.delete()
    current_app.db.session.commit()
    return EntrySchema(many=True).jsonify({}), 200


@api_entries.route("/api/v1/entries/<int:pk>", methods=["PUT"])
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


@api_entries.route("/api/v1/entries", methods=["POST"])
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
