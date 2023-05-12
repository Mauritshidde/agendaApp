import datetime, os, hashlib

# from validate_email_address import validate_email

from flask import Flask, render_template, url_for, redirect, request, session, make_response
from forms import signupForm, loginForm
from database_functies import add_user, authenticate

from flask_sqlalchemy import SQLAlchemy


from datetime import timedelta
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fe6ae17c6b7be3f5f9749130321b1baf'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.permanent_session_lifetime = datetime.timedelta(days=31)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = signupForm()
    
    bool_error = False
    message = ''

    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            if confirm_password == password:
                if add_user(email, username, password):
                    return(redirect('login'))
                else:
                    return(redirect('signup'))
            else:
                return(redirect('/'))


    return render_template('signup.html', title='signup', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()

    if form.validate_on_submit():
        username = request.form.get('username')
        if authenticate(username, request.form.get('password')):
            session['logged_in'] = True
            session['username'] = username
            return(redirect('/'))
        else:
            # wrong login
            print("niet ingelogd")

    return render_template('login.html', title='login', form=form)



@app.route('/')
def index():
    if session.get('logged_in'):
        return render_template('index.html', title='Login')
    else:
        return(redirect('/login'))




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
