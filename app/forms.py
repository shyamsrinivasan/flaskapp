from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    """Form for contacting creator"""

    name = StringField('Name', [DataRequired()])
    email = EmailField('Email', [Email(message='Not a valid email address'), DataRequired()])
    body = TextAreaField('Message', [DataRequired(), Length(min=4, message='your message is too short')])

    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

