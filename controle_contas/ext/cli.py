from controle_contas.ext.db.commands import create_db, drop_db
from controle_contas.ext.auth.commands import create_admin_user


def init_app(app):

    app.cli.add_command(app.cli.command()(create_db))
    app.cli.add_command(app.cli.command()(drop_db))
    app.cli.add_command(app.cli.command()(create_admin_user))
