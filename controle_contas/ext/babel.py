import babel
from flask_babelex import Babel


babel = Babel()


def init_app(app):

    babel.init_app(app)
