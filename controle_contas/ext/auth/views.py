from flask import Blueprint, render_template  # noqa


auth = Blueprint("auth", __name__)


@auth.route("/")
def index():
    return render_template("index.html")
