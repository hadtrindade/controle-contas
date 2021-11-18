from controle_contas.ext.db import db
from datetime import datetime


class Source(db.Model):
    __tablename__ = "source"

    id = db.Column("id", db.Integer, primary_key=True)
    description = db.Column("description", db.String(100), nullable=False)
    id_user = db.Column(
        "id_user",
        db.Integer,
        db.ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
    )
    entry = db.relationship(
        "Entry", backref="source", passive_deletes="all", lazy=True
    )

    def __repr__(self) -> str:
        return self.description


class Entry(db.Model):
    __tablename__ = "entry"

    id = db.Column("id", db.Integer, primary_key=True)
    description = db.Column("description", db.String(100), nullable=False)
    value = db.Column("value", db.Numeric, nullable=False)
    quantum = db.Column("quantum", db.Integer, default=1)
    revenue = db.Column("revenue", db.Boolean, default=False)
    id_user = db.Column(
        "id_user", db.Integer, db.ForeignKey("user.id", ondelete="CASCADE")
    )
    id_source = db.Column(
        "id_source", db.Integer, db.ForeignKey("source.id", ondelete="CASCADE")
    )
    id_group = db.Column(
        "id_group", db.Integer, db.ForeignKey("groups.id", ondelete="CASCADE")
    )
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return self.description


class Invoice(db.Model):
    __tablename__ = "invoice"

    id = db.Column("id", db.Integer, primary_key=True)
    description = db.Column("description", db.String(100), nullable=False)
    total = db.Column("total", db.Numeric)
    total_revenue = db.Column("total_revenue", db.Numeric)
    id_user = db.Column(
        "id_user", db.Integer, db.ForeignKey("user.id", ondelete="CASCADE")
    )
    detailed_invoice = db.relationship(
        "DetailedInvoice", backref="invoice", passive_deletes="all", lazy=True
    )

    def __repr__(self) -> str:
        return self.description


class DetailedInvoice(db.Model):
    __tablename__ = "detailed_invoice"

    id = db.Column("id", db.Integer, primary_key=True)
    description = db.Column("description", db.String())
    source = db.Column("source", db.String())
    value = db.Column("value", db.Numeric)
    revenue = db.Column("revenue", db.Boolean)
    id_invoice = db.Column(
        "id_invoice",
        db.Integer,
        db.ForeignKey("invoice.id", ondelete="CASCADE"),
    )
    id_group = db.Column(
        "id_group",
        db.Integer,
        db.ForeignKey("groups.id", ondelete="CASCADE"),
    )

    def __repr__(self) -> str:
        return self.description


class Wallet(db.Model):

    __tablename__ = "wallet"

    id = db.Column("id", db.Integer, primary_key=True)
    description = db.Column("description", db.String(), nullable=False)
    value = db.Column("value", db.Numeric)
    id_user = db.Column(
        "id_user", db.Integer, db.ForeignKey("user.id", ondelete="CASCADE")
    )

    def __repr__(self) -> str:
        return self.description


class Groups(db.Model):
    __tablename__ = "groups"

    id = db.Column("id", db.Integer, primary_key=True)
    description = db.Column("description", db.String(), nullable=False)
    id_user = db.Column(
        "id_user", db.Integer, db.ForeignKey("user.id", ondelete="CASCADE")
    )
    entry = db.relationship(
        "Entry", backref="groups", passive_deletes="all", lazy=True
    )
    detailed_invoice = db.relationship(
        "DetailedInvoice", backref="groups", passive_deletes="all", lazy=True
    )

    def __repr__(self) -> str:
        return self.description
