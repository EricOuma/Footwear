from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, URL, Optional

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = IntegerField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    send = SubmitField('Send Now')