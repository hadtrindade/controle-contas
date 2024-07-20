from flask import redirect, url_for
from flask_login import AnonymousUserMixin, LoginManager

from controle_contas.ext.auth.models import User

login_manager = LoginManager()


class CCAnonymousUser(AnonymousUserMixin):
    @property
    def is_staff(self):
        return False


def init_app(app):

    login_manager.init_app(app)
    login_manager.anonymous_user = CCAnonymousUser

    @login_manager.user_loader
    def load_user(user_id):
        return app.db.session.query(User).get(user_id)

    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for("site.login"))
