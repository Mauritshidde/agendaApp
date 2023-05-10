import datetime

from flask import Flask, render_template, url_for, redirect, request, session, make_response
from forms import signupForm
from database_functies import add_user

from flask_sqlalchemy import SQLAlchemy


from datetime import timedelta
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd1cabe24c9d3r5813ba8g81bd1082f2f'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.permanent_session_lifetime = datetime.timedelta(days=31)

# class Todo(db.model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.strong)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = signupForm()
    
    bool_error = False
    message = ''

    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form.get('username')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            print(email, username, password, confirm_password)

            if confirm_password == password:
                pass
            else:
                return(redirect('signup'))

            if not username_exists(username):
                add_user(request.form.get('email'), username, password)
            else:
                return(redirect('signup'))

            

    return render_template('signup.html', title='signup', form=form)

@app.route('/')
def index():

    return render_template('index.html', title='Login')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
