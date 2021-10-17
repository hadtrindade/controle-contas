from controle_contas.ext.serializer import ma
from marshmallow import fields
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
    first_name = fields.String()
    last_name = first_name = fields.String()
    email = fields.Email(required=True)
    password = fields.String(required=True)
    admin = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class EntrySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Entry

    id = fields.Integer()
    description = fields.String(required=True)
    value = fields.Decimal(required=True)
    quantum = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    id_source = fields.Integer()
    revenue = fields.Boolean()
