from werkzeug.security import generate_password_hash
from controle_contas.ext.db import db
from controle_contas.ext.serializer.models import UserSchema


def create_admin_user():
    """Create superuser"""

    data = {
        "username": "admin",
        "first_name": "Admin",
        "last_name": "Superuser",
        "email": "test@admin.com",
        "password": generate_password_hash("123"),
        "admin": True,
    }

    user = UserSchema().load(data)
    db.session.add(user)
    db.session.commit()
