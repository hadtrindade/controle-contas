from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from controle_contas.ext.db import db
from controle_contas.ext.serializer.models import UserSchema


def create_admin_user():
    """Create superuser"""

    data = {
        "username": "admin",
        "first_name": "Admin",
        "last_name": "Superuser",
        "email": "admin@admin.com",
        "password": generate_password_hash("admin"),
        "admin": True,
    }
    try:
        user = UserSchema().load(data)
        db.session.add(user)
        db.session.commit()
        print("Created")
    except IntegrityError as e:
        print(e)
