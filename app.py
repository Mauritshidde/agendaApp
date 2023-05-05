from flask import Flask, render_template, url_for, redirect, request, session, make_response
from forms import signupForm

from flask_sqlalchemy import SQLAlchemy

import datetime
from datetime import timedelta
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd1cabe24c9d3r5813ba8g81bd1082f2f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

app.permanent_session_lifetime = datetime.timedelta(days=31)

# class Todo(db.model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.strong)

@app.route('/signup')
def signup():
    form = signupForm()


    return render_template('signup.html', title='signup', form=form)

@app.route('/')
def index():

    return render_template('index.html', title='Login')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
