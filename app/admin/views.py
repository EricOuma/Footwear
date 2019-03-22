import cloudinary.uploader

from flask import current_app, abort, render_template, redirect, url_for
from flask_login import current_user, login_required


from app import db
from . import admin
from .forms import ShoeForm, BrandForm
from app.decorators import is_admin
from app.models import Shoe, Brand, ShoeSize

# add admin dashboard view
@admin.route('/dashboard')
@login_required
@is_admin
def admin_dashboard():
    return render_template('admin/admin_dashboard.html', title="Dashboard")

@admin.route('/add_brand', methods=['GET', 'POST'])
@login_required
@is_admin
def add_brand():
    form = BrandForm()
    if form.validate_on_submit():
        brand_logo = cloudinary.uploader.upload(form.brand_logo.data)
        brand = Brand(name=form.name.data, description=form.description.data, website = form.website.data, logo_id = brand_logo['public_id'], logo_url = brand_logo['secure_url'])

        db.session.add(brand)
        db.session.commit()

        return redirect(url_for('.add_brand'))
    return render_template('admin/add_brand.html', form=form, title="Dashboard")

@admin.route('/add_shoe', methods=['GET', 'POST'])
@login_required
@is_admin
def add_shoe():
    form = ShoeForm()
    form.brand.choices = [('0', 'Select')]+[(brand.id, brand.name) for brand in Brand.query.order_by('name')]
    if form.validate_on_submit():
        shoe_image = cloudinary.uploader.upload(form.shoe_image.data)
        shoe = Shoe(name=form.name.data, description=form.description.data, price=form.price.data, size = ShoeSize[form.size.data].value, quantity=form.quantity.data, brand_id=form.brand.data, image_id = shoe_image['public_id'], image_url = shoe_image['secure_url'])

        db.session.add(shoe)
        db.session.commit()

        return redirect(url_for('.add_shoe'))
    return render_template('admin/add_shoe.html', form=form, title="Dashboard")

@admin.route('/shoes')
@login_required
@is_admin
def all_shoes():
    shoes = Shoe.query.all()
    return render_template('admin/shoes.html', shoes=shoes)


@admin.route('/brands')
@login_required
@is_admin
def all_brands():
    brands = Brand.query.all()
    return render_template('admin/brands.html', brands=brands)

@admin.route('/shoes/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@is_admin
def edit_shoe(id):
    shoe = Shoe.query.get_or_404(id)
    form = ShoeForm(obj=shoe)
    del form.shoe_image
    form.brand.choices = [('0', 'Select')]+[(brand.id, brand.name) for brand in Brand.query.order_by('name')]
    if form.validate_on_submit():
        shoe.name = form.name.data
        shoe.descrption = form.description.data
        shoe.size = ShoeSize[form.size.data].value
        shoe.quantity = form.quantity.data
        shoe.price = form.price.data
        shoe.brand_id = form.brand.data
        # form.populate_obj(shoe)

        db.session.commit()
        
        return redirect(url_for('.all_shoes'))
    
    

    return render_template('admin/add_shoe.html', form=form, edit=True)

@admin.route('/brands/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@is_admin
def edit_brand(id):
    brand = Brand.query.get_or_404(id)
    form = BrandForm(obj=brand)
    del form.brand_logo
    if form.validate_on_submit():
        brand.name = form.name.data
        brand.description = form.description.data
        brand.website = form.website.data

        db.session.commit()

        return redirect(url_for('.all_brands'))
    return render_template('admin/add_brand.html', form=form, edit=True)

@admin.route('/shoes/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@is_admin
def delete_shoe(id):
    shoe = Shoe.query.get_or_404(id)
    cloudinary.uploader.destroy(shoe.image_id, invalidate=True)
    Shoe.delete(shoe)
    return redirect(url_for('.all_shoes'))

@admin.route('/brands/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@is_admin
def delete_brand(id):
    brand = Brand.query.get_or_404(id)
    cloudinary.uploader.destroy(brand.logo_id, invalidate=True)
    Brand.delete(brand)
    return redirect(url_for('.all_brands'))