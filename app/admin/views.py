from flask import current_app, abort, render_template, redirect, url_for
from flask_login import current_user, login_required

from app import db
from . import admin
from .forms import ProductForm
from app.decorators import is_admin
from app.models import Shoe

# add admin dashboard view
@admin.route('/dashboard')
@login_required
@is_admin
def admin_dashboard():
    return render_template('admin/admin_dashboard.html', title="Dashboard")

@admin.route('/add_product', methods=['GET', 'POST'])
@login_required
@is_admin
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        shoe = Shoe(name=form.name.data, description=form.description.data, price=form.price.data)
        print(shoe)

        db.session.add(shoe)
        db.session.commit()

        return redirect(url_for('.add_product'))
    return render_template('admin/add_product.html', form=form, title="Dashboard")