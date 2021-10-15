import ast
from os import EX_CANTCREAT
from flask import Blueprint, current_app, request
from controle_contas.ext.serializer.models import SourceSchema
from marshmallow import ValidationError
from controle_contas.ext.db.models import Source


api_sources = Blueprint("api_sources", __name__)


@api_sources.route("/api/v1/sources", methods=["GET"])
def get_sources():
    query = Source.query.all()
    if not query:
        return SourceSchema().jsonify(query), 204
    return SourceSchema(many=True).jsonify(query), 200


@api_sources.route("/api/v1/sources/<int:pk>", methods=["GET"])
def get_source(pk):
    query = Source.query.filter(Source.id == pk)
    if not query.first():
        return SourceSchema().jsonify(query), 204
    return SourceSchema(many=True).jsonify(query), 200


@api_sources.route("/api/v1/sources/<int:pk>", methods=["DELETE"])
def del_source(pk):

    query = Source.query.filter(Source.id == pk)
    if not query.first():
        return SourceSchema().jsonify({}), 404
    query.delete()
    current_app.db.session.commit()
    return SourceSchema(many=True).jsonify({}), 200


@api_sources.route("/api/v1/sources/<int:pk>", methods=["PUT"])
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


@api_sources.route("/api/v1/sources", methods=["POST"])
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
