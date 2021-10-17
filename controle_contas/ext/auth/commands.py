from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from werkzeug.security import generate_password_hash
from controle_contas.ext.auth.models import User
from controle_contas.ext.db import db
from controle_contas.ext.serializer.models import UserSchema
from email_validator import validate_email, EmailNotValidError


def email_validate():

    while True:
        email = input("Digite seu email: ")
        try:
            result = validate_email(email)
            break
        except EmailNotValidError as err:
            print(str(err))
    return result.email


def validate_password():

    while True:
        password_1 = input("Digite a senha: ")
        password_2 = input("Digite novamente a senha: ")
        if password_1 == password_2:
            break
        print("As senhas não conferem! Difite novamente.")
    return generate_password_hash(password_1)


def create_user():
    """Create user"""

    data = {
        "username": input("Digite seu username: "),
        "first_name": input("Digite seu First Name: "),
        "last_name": input("Digite seu Last Name: "),
        "email": email_validate(),
        "password": validate_password(),
        "admin": True,
    }
    try:
        data_is_valid = UserSchema().load(data)
        user = [User(**data_is_valid)]
        db.session.bulk_save_objects(user)
        db.session.commit()
        print("Usuario Criado")
    except ValidationError as err:
        print(err.normalized_messages())
    except IntegrityError as err:
        print(err.orig.args)
