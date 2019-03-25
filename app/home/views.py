from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from . import home
from app.models import Customer, Shoe, ShoeSize, Brand


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
    return render_template('home/shoes.html', shoes=shoes, brands=brands, sizes=sizes, title="Shop", active='shoes')

@home.route('/add', methods=['GET', 'POST'])
def add():
    """
    Route for adding shoes to cart
    """
    return render_template('home/cart.html', title="Shop")