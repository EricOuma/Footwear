from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Customer(UserMixin, db.Model):
    """
    Create an Customer table
    """

    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    phone = db.Column(db.String(10), index=True, unique=True)
    # gender
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Customer: {}>'.format(self.first_name + self.last_name)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))


class Shoe(db.Model):
    """
    Create a Shoe table
    """

    __tablename__ = 'shoes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    # size = db.Column(db.Integer)
    # image_url
    # colour

    def __repr__(self):
        return '<Shoe: {}>'.format(self.name)

