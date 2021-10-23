from flask_wtf import FlaskForm
from wtforms import fields, validators, PasswordField
from wtforms.fields.html5 import EmailField


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
