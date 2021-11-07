from flask_wtf import FlaskForm
from wtforms import (
    fields,
    validators,
    PasswordField,
    SelectField,
    BooleanField,
)
from wtforms.fields.html5 import EmailField, DecimalField, IntegerField


class RegisterForm(FlaskForm):

    username = fields.StringField(
        "Nome de Usuário", validators=[validators.DataRequired()]
    )
    first_name = fields.StringField(
        "Nome", validators=[validators.DataRequired()]
    )
    last_name = fields.StringField(
        "Sobrenome", validators=[validators.DataRequired()]
    )
    email = EmailField(
        "Email address", [validators.DataRequired(), validators.Email()]
    )

    password = PasswordField(
        "Senha",
        [
            validators.DataRequired(),
            validators.EqualTo("confirm", message="As senhas não conferem"),
        ],
    )
    confirm = PasswordField("Repita a senha")


class EntriesForm(FlaskForm):

    description = fields.StringField(
        "Descrição", validators=[validators.DataRequired()]
    )
    value = DecimalField(
        "Valor", places=2, validators=[validators.DataRequired()]
    )
    quantum = IntegerField("Parcela", validators=[validators.DataRequired()])
    id_source = SelectField(
        "Origem", coerce=int, validators=[validators.DataRequired()]
    )
    revenue = BooleanField("Receita?", false_values=(False, "false", ""))


class SourcesForm(FlaskForm):

    description = fields.StringField(
        "Descrição", validators=[validators.DataRequired()]
    )


class InvoiceForm(FlaskForm):
    ...
