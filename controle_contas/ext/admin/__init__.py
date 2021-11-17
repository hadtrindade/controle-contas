from flask_admin import Admin
from controle_contas.ext.db.models import (
    Source,
    Entry,
    Invoice,
    Groups,
    Wallet,
)
from controle_contas.ext.auth.models import User
from controle_contas.ext.admin.model_view import (
    UserModelView,
    SourceModelView,
    EntryModelView,
    CeAdminIndexView,
    InvoiceModelView,
    GroupsModelView,
    WalletModelView,
)


admin = Admin()


def init_app(app):

    admin.name = app.config["ADMIN_NAME"] = "Controle de Contas"
    admin.template_mode = "bootstrap4"
    admin.base_template = "admin/controle_contas_acess_control.html"
    admin.init_app(app, index_view=CeAdminIndexView())

    admin.add_view(UserModelView(User, app.db.session))
    admin.add_view(WalletModelView(Wallet, app.db.session))
    admin.add_view(GroupsModelView(Groups, app.db.session))
    admin.add_view(SourceModelView(Source, app.db.session))
    admin.add_view(EntryModelView(Entry, app.db.session))
    admin.add_view(InvoiceModelView(Invoice, app.db.session))
