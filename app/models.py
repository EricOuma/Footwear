from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum, unique
from datetime import datetime
from jinja2 import Template

from app import db, login_manager

@unique
class ShoeSize(Enum):
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    ELEVEN = 11

@unique
class ClothSize(Enum):
    xs = 'XS'
    s = 'S'
    m = 'M'
    l = 'L'
    xl = 'XL'
    xxl = 'XXL'

# template = Template('{{ ShoeSize[db_value].value }} == {{ db_value }}')
# template.globals['ShoeSize'] = ShoeSize
# template.render(db_value='FIVE')

cart_shoes = db.Table('cart_shoes',
    db.Column('shoe_id', db.Integer, db.ForeignKey('shoes.id'), primary_key=True),
    db.Column('customer_id', db.Integer, db.ForeignKey('customers.id'), primary_key=True)
)

cart_clothes = db.Table('cart_clothes',
    db.Column('cloth_id', db.Integer, db.ForeignKey('clothes.id'), primary_key=True),
    db.Column('customer_id', db.Integer, db.ForeignKey('customers.id'), primary_key=True)
)

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
    gender = db.Column(db.String(6))
    password_hash = db.Column(db.String(128))
    cart_shoes = db.relationship('Shoe', secondary=cart_shoes, backref=db.backref('cart_shoes', lazy='dynamic'), lazy='dynamic')
    cart_clothes = db.relationship('Cloth', secondary=cart_clothes, backref=db.backref('cart_clothes', lazy='dynamic'), lazy='dynamic')

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

    @staticmethod
    def is_admin(self):
        return self.email == current_app.config['ADMIN_EMAIL']

    def __repr__(self):
        return '<Customer: {}>'.format(self.first_name + self.last_name)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Customer.query.get(int(user_id))


class AnonymousUser(AnonymousUserMixin):
    """Class for Anonymous users"""
    def __init__(self):
        self.email = None

    def is_admin(self):
        return False

login_manager.anonymous_user = AnonymousUser

class Shoe(db.Model):
    """
    Create a Shoe table
    """

    __tablename__ = 'shoes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    size = db.Column(db.String(6))
    quantity = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
    image_id = db.Column(db.String(30))
    image_url = db.Column(db.String(200))
    # colour

    @staticmethod
    def delete(self):
        """For deleting a shoe"""
        if self:
            db.session.delete(self)
            db.session.commit()

    def __repr__(self):
        return self.name


class Cloth(db.Model):
    """
    Create a cloth table
    """

    __tablename__ = 'clothes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    size = db.Column(db.String(6))
    quantity = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    image_id = db.Column(db.String(30))
    image_url = db.Column(db.String(200))
    # colour

    @staticmethod
    def delete(self):
        """For deleting a cloth"""
        if self:
            db.session.delete(self)
            db.session.commit()

    def __repr__(self):
        return self.name
class Brand(db.Model):
    """
    Create a Brand table
    """

    __tablename__ = 'brands'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    description = db.Column(db.Text)
    website = db.Column(db.String(30))
    logo_id = db.Column(db.String(30))
    logo_url = db.Column(db.String(200))
    shoes = db.relationship('Shoe', backref='brand', lazy='dynamic')

    @staticmethod
    def delete(self):
        """For deleting a brand"""
        if self:
            db.session.delete(self)
            db.session.commit()

    def __repr__(self):
        return self.name