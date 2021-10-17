from flask_admin import Admin
from controle_contas.ext.db.models import Source, Entry
from controle_contas.ext.auth.models import User
from controle_contas.ext.admin.model_view import (
    UserModelView,
    SourceModelView,
    EntryModelView,
    CeAdminIndexView,
)


admin = Admin()


def init_app(app):

    admin.name = app.config["ADMIN_NAME"] = "Controle de Contas"
    admin.template_mode = "bootstrap4"
    admin.base_template = "my_master.html"
    admin.init_app(app, index_view=CeAdminIndexView())

    admin.add_view(SourceModelView(Source, app.db.session))
    admin.add_view(EntryModelView(Entry, app.db.session))
    admin.add_view(UserModelView(User, app.db.session))
