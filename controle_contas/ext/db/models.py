from controle_contas.ext.db import db
from datetime import datetime


class Source(db.Model):
    __tablename__ = "Source"
    id = db.Column("id", db.Integer, primary_key=True)
    description = db.Column("description", db.String(100), nullable=False)
    id_user = db.Column("id_user", db.Integer, db.ForeignKey("User.id"))

    user = db.relationship("User", foreign_keys=id_user)

    def __repr__(self) -> str:
        return self.description


class Entry(db.Model):
    __tablename__ = "Entry"

    id = db.Column("id", db.Integer, primary_key=True)
    description = db.Column("description", db.String(100), nullable=False)
    value = db.Column("value", db.Numeric, nullable=False)
    quantum = db.Column("quantum", db.Integer, default=1)
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime)
    id_source = db.Column("id_source", db.Integer, db.ForeignKey("Source.id"))
    revenue = db.Column("revenue", db.Boolean)

    source = db.relationship("Source", foreign_keys=id_source)

    def __repr__(self) -> str:
        return self.description
