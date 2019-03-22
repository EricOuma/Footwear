from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, IntegerField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, URL, Optional


from app.models import ShoeSize, Brand
class ShoeForm(FlaskForm):
    """
    Form for admin to add new shoe
    """
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    brand = SelectField('Brand', validators=[DataRequired()], coerce=int)
    price = IntegerField('Price', validators=[DataRequired()])
    size = SelectField('Shoe size', choices=[('', 'Select Shoe size')]+[(name, member.value) for name, member in ShoeSize.__members__.items()], validators=[DataRequired()])
    quantity = IntegerField('Quantity',  validators=[DataRequired()])
    shoe_image = FileField('Shoe Image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'svg', 'webp'], 'Images only!')])
    submit = SubmitField('Save')


class BrandForm(FlaskForm):
    """
    Form for admin to add new brand
    """
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    website = StringField('Website', validators=[Optional(), URL()])
    brand_logo = FileField('Brand Logo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'svg', 'webp'], 'Images only!')])
    submit = SubmitField('Save')