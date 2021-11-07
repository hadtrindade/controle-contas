from controle_contas.ext.db import db
from sqlalchemy.orm import backref
from datetime import datetime



class Source(db.Model):
    __tablename__ = "source"

    id = db.Column("id", db.Integer, primary_key=True)
    description = db.Column("description", db.String(100), nullable=False)
    id_user = db.Column(
        "id_user", db.Integer, db.ForeignKey("user.id"), nullable=False
    )
    entry = db.relationship("Entry", backref="source", lazy=True)

    def __repr__(self) -> str:
        return self.description


class Entry(db.Model):
    __tablename__ = "entry"

    id = db.Column("id", db.Integer, primary_key=True)
    description = db.Column("description", db.String(100), nullable=False)
    value = db.Column("value", db.Numeric, nullable=False)
    quantum = db.Column("quantum", db.Integer, default=1)
    revenue = db.Column("revenue", db.Boolean, default=False)
    id_user = db.Column("id_user", db.Integer, db.ForeignKey("user.id"))
    id_source = db.Column("id_source", db.Integer, db.ForeignKey("source.id"))
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return self.description


class Invoice(db.Model):
    __tablename__ = "invoice"

    id = db.Column("id", db.Integer, primary_key=True)
    description = db.Column(
        "description", db.String(100), nullable=False, unique=True
    )
    total = db.Column("total", db.Numeric)
    total_revenue = db.Column("total_revenue", db.Numeric)
    id_user = db.Column("id_user", db.Integer, db.ForeignKey("user.id"))
    detailed_invoice = db.relationship("DetailedInvoice", backref="invoice", cascade="all, delete-orphan", lazy=True)

    def __repr__(self) -> str:
        return self.description


class DetailedInvoice(db.Model):
    __tablename__ = "detailed_invoice"

    id = db.Column("id", db.Integer, primary_key=True)
    description = db.Column("description", db.String(), nullable=False)
    value = db.Column("value", db.Numeric)
    revenue = db.Column("revenue", db.Boolean)
    id_invoice = db.Column(
        "id_invoice", db.Integer, db.ForeignKey("invoice.id")
    )


    def __repr__(self) -> str:
        return self.description
