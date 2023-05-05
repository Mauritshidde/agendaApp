from flask_wtf import FlaskForm
import email_validator
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectMultipleField, RadioField, IntegerField
from wtforms.validators import InputRequired, DataRequired, EqualTo, NumberRange, Email


class signupForm(FlaskForm):
    email = StringField('', validators=[DataRequired('please enter your email adress'), Email('this field requires an valid email adress')])
    username = StringField('', validators=[DataRequired('please enter an username'), NumberRange(min=1, max=20)])
    password = PasswordField('', validators=[DataRequired('please enter an password'), EqualTo('conform_password', message='Passwords must match')])
    confirm_password = PasswordField('', validators=[DataRequired('please enter your password again')])
    submit = SubmitField('create acount')
