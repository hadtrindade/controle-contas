from flask import current_app
from flask_wtf import FlaskForm
from wtforms import fields, validators

from controle_contas.ext.auth.models import User


class LoginForm(FlaskForm):
    username = fields.StringField(
        validators=[validators.DataRequired()],
        render_kw={"placeholder": "Username"},
    )
    password = fields.PasswordField(
        validators=[validators.DataRequired()],
        render_kw={"placeholder": "Password"},
    )

    def get_user(self):
        return (
            current_app.db.session.query(User)
            .filter_by(username=self.username.data)
            .one_or_none()
        )
