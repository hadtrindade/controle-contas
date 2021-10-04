from flask import Blueprint, current_app, render_template #noqa


admin = Blueprint("admin", __name__)


@admin.route("/admin")
def index():
    return "teste"
