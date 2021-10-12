from controle_contas.ext.db import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        "username", db.String(100), unique=True, nullable=False
    )
    email = db.Column("email", db.String(100), unique=True, nullable=False)
    passwd = db.Column("passwd", db.String(50), nullable=False)
    admin = db.Column("admin", db.Boolean, default=False)
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime)

    def __repr__(self) -> str:
        return f"<User {self.username}>"
