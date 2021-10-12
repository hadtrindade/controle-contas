import json
from flask import Blueprint, jsonify, current_app, request
from controle_contas.ext.serializer.models import SourceSchema, UserSchema
from controle_contas.ext.db.models import Source
from controle_contas.ext.auth.models import User


api = Blueprint("api", __name__)


@api.route("/api/v1/sources", methods=["GET", "POST"])
def view_source():
    if request.method == "GET":
        sources = Source.query.all()
        return SourceSchema(many=True).jsonify(sources)
    elif request.method == "POST":
        source_schema = SourceSchema()
        source, error = source_schema.loads(request.json)
        if error:
            return jsonify(error), 422
        current_app.db.session.add(source)
        current_app.db.session.commit()
        return source_schema.jsonify(source), 201


@api.route("/api/v1/users", methods=["GET", "POST"])
def view_users():
    if request.method == "GET":
        users = User.query.all()
        return UserSchema(many=True).jsonify(users)
    elif request.method == "POST":
        user_schema = UserSchema()
        print(request.json)
        user = user_schema.loads(request.json)
        # import ipdb; ipdb.set_trace()
        if not user:
            return jsonify({"vemos": "já"}), 422
        u = User(**user)
        current_app.db.session.add(u)
        current_app.db.session.commit()
        return user_schema.jsonify(user), 201
