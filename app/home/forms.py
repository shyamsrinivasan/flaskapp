from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, EmailField, TextAreaField, SubmitField, PasswordField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class ContactForm(FlaskForm):
    """Form for contacting creator"""

    name = StringField('Name', [DataRequired()])
    email = EmailField('Email', [Email(message='Not a valid email address'), DataRequired()])
    body = TextAreaField('Message', [DataRequired(), Length(min=4, message='Your message is too short')])

    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    """Form to signup as an user in application"""

    first_name = StringField('First Name', [DataRequired(message='Please provide your first name')])
    last_name = StringField('Last Name', [DataRequired(message='Please provide your last name')])
    name = StringField('Username', [DataRequired(),
                                    Length(min=6, message='Your username should be minimum 6 characters')])
    password = PasswordField('Password', [DataRequired(message='Please enter a password'),
                                          Length(min=8, message='Password should be at least 8 characters')])
    confirm_pass = PasswordField('Confirm Password', [EqualTo(password, message='Passwords must match')])
    employee_type = SelectField('Employee Type', [DataRequired()], choices=[('Administrator', 'admin'),
                                                                            ('User', 'user'),
                                                                            ('Hybrid', 'hybrid')])
    dob = DateField('Date of Birth', [DataRequired()])

    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


