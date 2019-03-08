from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

class ProductForm(FlaskForm):
    """
    Form for admin to add new product
    """
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    submit = SubmitField('Save')