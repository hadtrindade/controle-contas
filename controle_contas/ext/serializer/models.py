from marshmallow import fields

from controle_contas.ext.auth.models import User
from controle_contas.ext.db.models import Entry, Invoice, Source
from controle_contas.ext.serializer import ma


class SourceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Source
        load_instance = True

    id = fields.Integer()
    description = fields.String(required=True)
    id_user = fields.Integer()


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = fields.Integer()
    username = fields.String(required=True)
    first_name = fields.String()
    last_name = first_name = fields.String()
    email = fields.Email(required=True)
    password = fields.String(required=True)
    admin = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()


class UserLoginSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    username = fields.String(required=True)
    password = fields.String(required=True)


class EntrySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Entry
        load_instance = True

    id = fields.Integer()
    description = fields.String(required=True)
    value = fields.Decimal(required=True)
    quantum = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    id_source = fields.Integer(required=True)
    id_user = fields.Integer(required=True)
    revenue = fields.Boolean()


class InvoiceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Invoice
        load_instance = True

    id = fields.Integer()
    description = fields.String(required=True)
    total = fields.Decimal(required=True)
    id_user = fields.Integer(required=True)

    def __repr__(self) -> str:
        return self.description
