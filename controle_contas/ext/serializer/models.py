from controle_contas.ext.serializer import ma
from marshmallow import fields, ValidationError
from controle_contas.ext.auth.models import User
from controle_contas.ext.db.models import Source, Entry


class SourceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Source

    id = fields.Integer()
    description = fields.String(required=True)
    id_user = fields.Integer()


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = fields.Integer()
    username = fields.String(required=True)
    email = fields.Email()
    passwd = fields.String(required=True)
    admin = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
