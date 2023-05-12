from flask_wtf import FlaskForm
import email_validator
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectMultipleField, RadioField, IntegerField, EmailField
from wtforms.validators import InputRequired, DataRequired, EqualTo, NumberRange, Length


class signupForm(FlaskForm):
    email = EmailField('enter your email adress', validators=[DataRequired('please enter your email adress')])
    username = StringField('username', validators=[DataRequired('please enter an username'), Length(min=6, max=20)])
    password = PasswordField('password', validators=[DataRequired('please enter an password')])
    confirm_password = PasswordField('confirm password', validators=[DataRequired('please enter your password again'), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('create acount')

class loginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired('Please enter your username'), Length(min=6, max=20)])
    password = PasswordField('password', validators=[DataRequired('Please enter your password')])
    submit = SubmitField('login')