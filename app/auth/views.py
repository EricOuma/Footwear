from flask import flash, redirect, render_template, url_for, current_app
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from app import db
from app.models import Customer


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an customer to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        customer = Customer(first_name=form.first_name.data, last_name=form.last_name.data, gender=form.gender.data, email=form.email.data, phone=form.phone.data, password=form.password.data)

        # add employee to the database
        db.session.add(customer)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        customer = Customer.query.filter_by(email=form.email.data).first()
        if customer is not None and customer.verify_password(
                form.password.data):
            # log employee in
            login_user(customer)

            # redirect to the appropriate dashboard page
            if Customer.is_admin(customer):
                return redirect(url_for('admin.admin_dashboard'))
            else:
                return redirect(url_for('home.index'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('home.index'))