from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    current_app,
    flash,
)
from flask_login import login_user, logout_user, login_required, current_user
from controle_contas.ext.admin.forms import LoginForm
from controle_contas.ext.site.forms import (
    RegisterForm,
    EntriesForm,
    SourcesForm,
    InvoiceForm,
)
from controle_contas.ext.auth.models import User
from controle_contas.ext.db.models import Entry, Source
from werkzeug.security import generate_password_hash, check_password_hash


site = Blueprint("site", __name__)


@site.route("/")
def index():
    return render_template("home.html")


@site.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        user = form.get_user()
        if user:
            if not user and not check_password_hash(
                user.password, form.password
            ):
                flash("Usuário ou senha inválidos!!!")
            login_user(user)

    if current_user.is_authenticated:
        return redirect(url_for("site.index"))

    return render_template("login.html", form=form)


@site.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        user = User(
            username=form.username.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=generate_password_hash(form.password.data),
            email=form.email.data,
        )
        current_app.db.session.add(user)
        current_app.db.session.commit()
        return redirect(url_for("site.login"))
    return render_template("register.html", form=form)


@site.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("site.index"))


@site.route("/dashboard")
@login_required
def dashboard():
    return redirect(url_for("site.index"))


@site.route("/add-entries", methods=["GET", "POST"])
@login_required
def add_entries():
    sources = Source.query.filter(Source.id_user == current_user.id).all()
    sources_list = [(s.id, s.description) for s in sources]
    form = EntriesForm(request.form)
    form.id_source.choices = sources_list
    if request.method == "POST" and form.validate_on_submit():
        entry = Entry(
            description=form.description.data,
            value=form.value.data,
            quantum=form.quantum.data,
            id_source=form.id_source.data,
            revenue=form.revenue.data,
        )
        current_app.db.session.add(entry)
        current_app.db.session.commit()
        return redirect(url_for("site.add_entries"))
    return render_template("entries.html", form=form)


@site.route("/add-sources", methods=["GET", "POST"])
@login_required
def add_sources():

    form = SourcesForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        source = Source(
            description=form.description.data,
            id_user=current_user.id,
        )
        current_app.db.session.add(source)
        current_app.db.session.commit()
        return redirect(url_for("site.add_sources"))
    return render_template("sources.html", form=form)


@site.route("/generate-invoice")
@login_required
def generate_invoice():
    return redirect(url_for("site.index"))


def init_app(app):
    app.register_blueprint(site)
