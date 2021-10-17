from flask_login import LoginManager
from controle_contas.ext.auth.models import User


login_manager = LoginManager()


def init_app(app):

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return app.db.session.query(User).get(user_id)
