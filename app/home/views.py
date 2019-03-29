from flask import render_template, redirect, url_for, abort
from flask_login import login_required, current_user
from sqlalchemy import func

from . import home
from app.models import Customer, Shoe, ShoeSize, Brand, Cloth, ClothSize


@home.route('/')
def index():
    """
    Render the home template on the / route
    """
    if Customer.is_admin(current_user):
        return redirect(url_for('admin.admin_dashboard'))
    return render_template('home/index.html', title="Welcome")

@home.route('/shoes')
def shoes():
    """
    Render the shoes template on the / route
    """
    sizes = [name for name, member in ShoeSize.__members__.items()]
    shoes = Shoe.query.all()
    brands = Brand.query.all()
    min_price = Shoe.query.with_entities(func.min(Shoe.price)).scalar()
    max_price = Shoe.query.with_entities(func.max(Shoe.price)).scalar()

    return render_template('home/shoes.html', shoes=shoes, brands=brands, shoe_sizes=sizes, title="Shop", min_price=min_price, max_price=max_price, active='shoes')


@home.route('/clothes')
def clothes():
    """
    Render the clothes template on the / route
    """
    sizes = [name for name, member in ClothSize.__members__.items()]
    clothes = Cloth.query.all()
    min_price = Cloth.query.with_entities(func.min(Cloth.price)).scalar()
    max_price = Cloth.query.with_entities(func.max(Cloth.price)).scalar()

    return render_template('home/clothes.html', clothes=clothes, cloth_sizes=sizes, title="Shop", min_price=min_price, max_price=max_price, active='clothes')

@home.route('/product/<string:class_name>/<int:id>')
def product(id, class_name):
    # The classname helps to get the model from which the product is to be fetched
    cloth_sizes = [name for name, member in ClothSize.__members__.items()]
    shoe_sizes = [name for name, member in ShoeSize.__members__.items()]
    cls_name = globals()[class_name]
    product = cls_name.query.get_or_404(id)

    return render_template('home/product.html', product=product, cloth_sizes=cloth_sizes, shoe_sizes=shoe_sizes)

@home.route('/add', methods=['GET', 'POST'])
def add():
    """
    Route for adding shoes to cart
    """
    return render_template('home/cart.html', title="Shop")