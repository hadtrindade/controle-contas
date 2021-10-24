from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from flask_admin import AdminIndexView
from controle_contas.ext.admin.forms import LoginForm
from flask import url_for, redirect, request, flash
from flask_admin import expose
from flask_login import current_user, login_user, logout_user
from werkzeug.security import check_password_hash


class UserModelView(ModelView):
    form_base_class = SecureForm
    page_size = 50
    can_view_details = True
    column_filters = ["username", "admin"]
    column_exclude_list = ["passwd", "created_at", "updated_at"]
    column_searchable_list = ["username", "email"]
    column_editable_list = ["username", "email"]
    create_modal = True
    edit_modal = True
    form_excluded_columns = ["created_at"]
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated


class SourceModelView(ModelView):
    form_base_class = SecureForm
    page_size = 50
    can_view_details = True
    create_modal = True
    edit_modal = True
    column_searchable_list = ["id_user", "description"]
    column_filters = ["id_user", "description"]
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated


class EntryModelView(ModelView):
    form_base_class = SecureForm
    page_size = 50
    can_view_details = True
    create_modal = True
    edit_modal = True
    column_searchable_list = ["id_source", "description"]
    column_filters = ["id_source", "description"]
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated


class CeAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for(".login_view"))
        return super(CeAdminIndexView, self).index()

    @expose("/login/", methods=(["GET", "POST"]))
    def login_view(self):

        form = LoginForm(request.form)

        if request.method == "POST" and form.validate_on_submit():
            user = form.get_user()
            if user and user.is_staff:
                if not user and not check_password_hash(
                    user.password, form.password
                ):
                    flash("Usuário ou senha inválidos!!!")
                login_user(user)

        if current_user.is_authenticated:
            return redirect(url_for(".index"))

        self._template_args["form"] = form
        return super(CeAdminIndexView, self).index()

    @expose("/logout/")
    def logout_view(self):
        logout_user()
        return redirect(url_for(".index"))
