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
    revenue = db.Column("revenue", db.Boolean)
    id_user = db.Column("id_user", db.Integer, db.ForeignKey("User.id"))
    id_source = db.Column("id_source", db.Integer, db.ForeignKey("Source.id"))
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime)

    user = db.relationship("User", foreign_keys=id_user)
    source = db.relationship("Source", foreign_keys=id_source)

    def __repr__(self) -> str:
        return self.description


class Invoice(db.Model):
    __tablename__ = "Invoice"

    id = db.Column("id", db.Integer, primary_key=True)
    description = db.Column("description", db.String(100), nullable=False)
    id_entry = db.Column("id_entry", db.Integer, db.ForeignKey("Entry.id"))

    entry = db.relationship("Entry", foreign_keys=id_entry)

    def __repr__(self) -> str:
        return self.description
