from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    if current_user.is_admin:
        return redirect(url_for('admin.admin_dashboard'))
    return render_template('home/index.html', title="Welcome")