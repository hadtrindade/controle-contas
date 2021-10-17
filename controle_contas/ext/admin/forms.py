from flask import current_app
from wtforms import form, fields, validators
from werkzeug.security import check_password_hash
from controle_contas.ext.auth.models import User


class LoginForm(form.Form):
    username = fields.StringField(validators=[validators.DataRequired()])
    password = fields.PasswordField(validators=[validators.DataRequired()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError("Invalid user")

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
            # to compare plain text passwords use
            # if user.password != self.password.data:
            raise validators.ValidationError("Invalid password")

    def get_user(self):
        return (
            current_app.db.session.query(User)
            .filter_by(username=self.username.data)
            .first()
        )
