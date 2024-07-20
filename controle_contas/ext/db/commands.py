from controle_contas.ext.db import db


def drop_db():
    """Cleans database"""
    db.drop_all()
