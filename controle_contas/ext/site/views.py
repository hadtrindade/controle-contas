from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    current_app,
    jsonify,
)
from flask.helpers import flash
from flask_login import login_user, logout_user, login_required, current_user
from controle_contas.ext.admin.forms import LoginForm
from controle_contas.ext.site.forms import (
    RegisterForm,
    EntriesForm,
    SourcesForm,
    InvoiceForm,
    GroupsForm,
)
from controle_contas.ext.auth.models import User
from controle_contas.ext.db.models import (
    Entry,
    Invoice,
    Source,
    DetailedInvoice,
    Groups,
)
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import desc
from dateutil.relativedelta import relativedelta
from datetime import date


site = Blueprint("site", __name__)


@site.context_processor
def date_invoice():
    return dict(date=date.today().strftime("%m-%y"))


@site.route("/")
def index():
    return render_template("home.html")


@site.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        user = form.get_user()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(
                    url_for(
                        "site.dashboard", desc=date.today().strftime("%m-%y")
                    )
                )
            flash("Senha inválida")
            return redirect(url_for("site.login"))
        else:
            flash("Usuário inválido")
            return redirect(url_for("site.login"))
    if current_user.is_authenticated:
        return redirect(
            url_for("site.dashboard", desc=date.today().strftime("%m-%y"))
        )
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


@site.route("/entries", methods=["GET", "POST"])
@login_required
def entries():
    entries = Entry.query.filter_by(id_user=current_user.id)
    return render_template("entries/entries.html", entries=entries)


# Entries


@site.route("/add-entries", methods=["GET", "POST"])
@login_required
def add_entries():
    sources = Source.query.filter_by(id_user=current_user.id).all()
    sources_list = [(s.id, s.description) for s in sources]
    groups = Groups.query.filter_by(id_user=current_user.id).all()
    groups_list = [(g.id, g.description) for g in groups]
    form = EntriesForm(request.form)
    form.id_group.choices = groups_list
    form.id_source.choices = sources_list
    if request.method == "POST" and form.validate_on_submit():
        entry = Entry(
            description=form.description.data,
            value=form.value.data,
            quantum=form.quantum.data,
            id_source=form.id_source.data,
            id_group=form.id_group.data,
            revenue=form.revenue.data,
            id_user=current_user.id,
        )
        current_app.db.session.add(entry)
        current_app.db.session.commit()
        return jsonify({"msg": "ok"}), 201
    return render_template("entries/form_entries.html", form=form)


@site.route("/edit-entries/<int:pk>", methods=["GET", "POST"])
@login_required
def edit_entries(pk):
    sources = Source.query.filter_by(id_user=current_user.id, id=pk).all()
    sources_list = [(s.id, s.description) for s in sources]
    groups = Groups.query.filter_by(id_user=current_user.id, id=pk).all()
    groups_list = [(g.id, g.description) for g in groups]
    query = Entry.query.filter_by(id=pk)
    form = EntriesForm(obj=query.first())
    form.id_group.choices = groups_list
    form.id_source.choices = sources_list

    if request.method == "POST" and form.validate_on_submit():
        query.update(
            {
                "description": form.description.data,
                "value": form.value.data,
                "quantum": form.quantum.data,
                "id_group": form.id_group.data,
                "id_source": form.id_source.data,
                "revenue": form.revenue.data,
                "id_user": current_user.id,
            }
        )
        current_app.db.session.commit()
        return jsonify({"msg": "ok"}), 200
    return render_template(
        "entries/form_update_entries.html", form=form, pk=query.first().id
    )


@site.route("/del-entries/<int:pk>", methods=["GET"])
@login_required
def del_entries(pk):
    query = Entry.query.filter(Entry.id == pk)
    if query.first():
        query.delete()
        current_app.db.session.commit()
        return jsonify({"msg": "ok"}), 200
    return jsonify({"error": "registro não encontrado"})


# SOURCES


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
        return jsonify({"msg": "ok"}), 201
    return render_template("sources/form_add_sources.html", form=form)


@site.route("/edit-sources/<int:pk>", methods=["GET", "POST"])
@login_required
def edit_sources(pk):
    query = Source.query.filter_by(id=pk, id_user=current_user.id)
    form = SourcesForm(obj=query.first())

    if request.method == "POST" and form.validate_on_submit():
        query.update({"description": form.description.data})
        current_app.db.session.commit()
        return jsonify({"msg": "ok"}), 200
    return render_template(
        "sources/form_update_sources.html", form=form, pk=query.first().id
    )


@site.route("/del-sources/<int:pk>", methods=["GET"])
@login_required
def del_sources(pk):
    query = Source.query.filter_by(id=pk, id_user=current_user.id)
    if query.first():
        query.delete()
        current_app.db.session.commit()
        return jsonify({"msg": "ok"}), 200
    return jsonify({"error": "registro não encontrado"})


@site.route("/sources", methods=["GET", "POST"])
@login_required
def sources():

    query = Source.query.filter_by(id_user=current_user.id).all()
    return render_template("sources/sources.html", source=query)


# Groups


@site.route("/groups", methods=["GET", "POST"])
@login_required
def groups():

    query = Groups.query.filter_by(id_user=current_user.id).all()
    print(query)
    return render_template("groups/groups.html", groups=query)


@site.route("/add-groups", methods=["GET", "POST"])
@login_required
def add_groups():

    form = GroupsForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        groups = Groups(
            description=form.description.data,
            id_user=current_user.id,
        )
        current_app.db.session.add(groups)
        current_app.db.session.commit()
        return jsonify({"msg": "ok"}), 201
    return render_template("groups/form_add_groups.html", form=form)


@site.route("/del-groups/<int:pk>", methods=["GET"])
@login_required
def del_groups(pk):
    query = Groups.query.filter_by(id=pk, id_user=current_user.id)
    if query.first():
        query.delete()
        current_app.db.session.commit()
        return jsonify({"msg": "ok"}), 200
    return jsonify({"erro": "registro não encontrado"})


@site.route("/edit-groups/<int:pk>", methods=["GET", "POST"])
@login_required
def edit_groups(pk):
    query = Groups.query.filter_by(id=pk, id_user=current_user.id)
    form = GroupsForm(obj=query.first())

    if request.method == "POST" and form.validate_on_submit():
        query.update({"description": form.description.data})
        current_app.db.session.commit()
        return jsonify({"msg": "ok"}), 200
    return render_template(
        "groups/form_update_groups.html", form=form, pk=query.first().id
    )


# INVOICES


def generate_full_invoice():
    detailed_invoice = {}
    entries = (
        Entry.query.filter_by(id_user=current_user.id)
        .order_by(desc(Entry.created_at))
        .all()
    )
    for e in entries:
        for x in range(e.quantum):
            date_m_y = e.updated_at + relativedelta(months=x)
            key = date_m_y.date().strftime("%m/%y")
            if key in detailed_invoice.keys():
                detailed_invoice[key]["details"].append(
                    {
                        "description": e.description,
                        "value": e.value,
                        "revenue": e.revenue,
                        "id_group": e.id_group,
                    }
                )
                if e.revenue:
                    detailed_invoice[key]["total_revenue"] += e.value
                else:
                    detailed_invoice[key]["total"] += e.value
            else:
                if e.revenue:
                    detailed_invoice[key] = {
                        "details": [
                            {
                                "description": e.description,
                                "value": e.value,
                                "revenue": e.revenue,
                                "id_group": e.id_group,
                            }
                        ],
                        "total": 0,
                        "total_revenue": e.value,
                    }
                else:
                    detailed_invoice[key] = {
                        "details": [
                            {
                                "description": e.description,
                                "value": e.value,
                                "revenue": e.revenue,
                                "id_group": e.id_group,
                            }
                        ],
                        "total": e.value,
                        "total_revenue": 0,
                    }

    return detailed_invoice


@site.route("/invoices", methods=["GET"])
@login_required
def get_invoices():

    invoices = Invoice.query.filter_by(id_user=current_user.id).all()
    return render_template(
        "invoices/invoice.html",
        invoices=invoices,
    )


@site.route("/invoices-details/<int:pk>", methods=["GET"])
@login_required
def get_datails(pk):
    query = DetailedInvoice.query.filter_by(id_invoice=pk).all()
    details = {}
    for i in query:
        if i.groups.description in details.keys():
            details[i.groups.description].append(i)
        else:
            details[i.groups.description] = [i]
    return render_template(
        "invoices/details.html",
        details=details,
        total=query[0].invoice.total,
        total_revenue=query[0].invoice.total_revenue,
        balance=(query[0].invoice.total_revenue - query[0].invoice.total),
    )


@site.route("/invoices-details-group/<int:pk>", methods=["GET"])
@login_required
def get_datails_invoice_group(pk):
    details = DetailedInvoice.query.filter_by(id_group=pk).all()
    total = 0
    total_revenue = 0
    for i in details:
        if not i.revenue:
            total += i.value
        else:
            total_revenue += i.value

    return render_template(
        "invoices/details.html",
        details=details,
        total=total,
        total_revenue=total_revenue,
        balance=(total_revenue - total),
    )


@site.route("/del-invoices/<int:pk>", methods=["GET"])
@login_required
def del_invoices(pk):
    query = Invoice.query.filter_by(id=pk)
    if query.one_or_none():
        query.delete()
        current_app.db.session.commit()
        return jsonify({"msg": "ok"}), 200
    return jsonify({"error": "registro não encontrado"})


@site.route("/generate-invoices", methods=["GET"])
@login_required
def generate_invoices():

    detailed_invoice = generate_full_invoice()
    Invoice.query.filter_by(id_user=current_user.id).delete()
    current_app.db.session.commit()

    data_invoices = []
    for k, v in detailed_invoice.items():

        data = {
            "description": k,
            "total": float(v["total"]),
            "total_revenue": float(v["total_revenue"]),
            "id_user": current_user.id,
        }
        data_invoices.append(Invoice(**data))
    current_app.db.session.add_all(data_invoices)
    current_app.db.session.commit()

    query_invoices = Invoice.query.filter_by(id_user=current_user.id).all()
    data_detailed_invoice = []
    for i in query_invoices:
        for j in detailed_invoice[i.description]["details"]:
            j["id_invoice"] = i.id
            data_detailed_invoice.append(DetailedInvoice(**j))
    current_app.db.session.add_all(data_detailed_invoice)
    current_app.db.session.commit()

    return redirect(url_for("site.get_invoices"))


@site.route("/dashboard/<desc>")
@login_required
def dashboard(desc):
    month = desc.replace("-", "/")
    invoice = Invoice.query.filter_by(
        id_user=current_user.id, description=month
    ).one_or_none()
    invoices = Invoice.query.filter_by(id_user=current_user.id).all()
    invoices_list = [(i.description, i.description) for i in invoices]
    form = InvoiceForm(request.form)
    form.invoices.choices = invoices_list

    if invoice:
        form.invoices.data = invoice.description
        query = DetailedInvoice.query.filter_by(id_invoice=invoice.id).all()
        details = {}
        for i in query:
            if i.groups.description in details.keys():
                details[i.groups.description].append(i)
            else:
                details[i.groups.description] = [i]
        return render_template(
            "dashboard.html",
            invoice=invoice,
            form=form,
            details=details,
            total=query[0].invoice.total,
            total_revenue=query[0].invoice.total_revenue,
            balance=(query[0].invoice.total_revenue - query[0].invoice.total),
        )
    return render_template(
        "dashboard.html",
        invoice=invoice,
        form=form,
        total=0,
        total_revenue=0,
        balance=0,
    )


def init_app(app):
    app.register_blueprint(site)
