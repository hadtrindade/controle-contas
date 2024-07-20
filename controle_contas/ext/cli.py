from controle_contas.ext.auth.commands import create_admin_user
from controle_contas.ext.db.commands import drop_db


def init_app(app):

    app.cli.add_command(app.cli.command()(drop_db))
    app.cli.add_command(app.cli.command()(create_admin_user))
