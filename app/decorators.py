from flask import current_app, abort
from flask_login import current_user
from functools import wraps

def is_admin(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        if current_user.email != current_app.config['ADMIN_EMAIL']:
            abort(403)
        return f(*args, **kwds)
    return wrapper