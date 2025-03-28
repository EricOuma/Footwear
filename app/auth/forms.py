from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, SelectField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Customer


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('', 'Select gender'), ('m', 'Male'), ('f', 'Female')], validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Customer.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')