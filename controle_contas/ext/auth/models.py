from datetime import datetime

from werkzeug.security import check_password_hash

from controle_contas.ext.db import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        "username", db.String(100), unique=True, nullable=False
    )
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column("email", db.String(100), unique=True, nullable=False)
    password = db.Column("password", db.String(), nullable=False)
    admin = db.Column("admin", db.Boolean, default=False)
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime)
    source = db.relationship(
        "Source", backref="user", passive_deletes="all", lazy=True
    )
    entry = db.relationship(
        "Entry", backref="user", passive_deletes="all", lazy=True
    )
    invoice = db.relationship(
        "Invoice", backref="user", passive_deletes="all", lazy=True
    )
    groups = db.relationship(
        "Groups", backref="user", passive_deletes="all", lazy=True
    )
    wallet = db.relationship(
        "Wallet", backref="user", passive_deletes="all", lazy=True
    )

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_staff(self):
        if self.admin:
            return True
        return False

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Required for administrative interface
    def __unicode__(self):
        return self.username

    def __repr__(self) -> str:
        return self.username
