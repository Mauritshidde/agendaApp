import datetime, os, hashlib

from datetime import date
import calendar

# from validate_email_address import validate_email

from flask import Flask, render_template, url_for, redirect, request, session, make_response, flash
from forms import signupForm, loginForm
from database_functies import add_user, authenticate, authenticated, get_random_string, add_session_to_db

from flask_sqlalchemy import SQLAlchemy


from datetime import timedelta
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fe6ae17c6b7be3f5f9749130321b1baf'
app.secret_key = 'fe6ae17c6b7be3f5f9749130321b1baf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.permanent_session_lifetime = datetime.timedelta(minutes=30)

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
    if request.method == 'POST':
    # if form.validate_on_submit():
        username = request.form.get('username')
        if authenticate(username, request.form.get('password')):
            session['logged_in'] = True
            # session_id = get_random_string(16)
            # add_session_to_db(session_id, username)
            # session['session_id'] = session_id
            session['username'] = username
            return(redirect('/'))
        else:
            # wrong login
            print("niet ingelogd")

    return render_template('login.html', title='login', form=form)



@app.route('/')
@authenticated
def index():
    # if session.get('logged_in'):
    #     return render_template('index.html', title='Login')
    # else:
    #     return(redirect('/login'))
    current_date = datetime.datetime.now()
    current_day = date.today()
    day_order = []
    day_numbers = []
    month_number = []

    month_lenght = calendar.monthrange(date.today().year, date.today().month)
    current_day_name =  calendar.day_name[current_day.weekday()]
    first_day_name =  calendar.day_name[month_lenght[0]]
    dict_lenght = month_lenght[1]

    for days in range(month_lenght[1]):
        day_order.append(calendar.day_name[current_date.replace(day=days+1).weekday()])
        day_numbers.append(days+1)
        month_number.append(date.today().month)

    # print(day_order)

    if (day_order[0] != 'Monday'):
        previous_month = current_date.replace(month=date.today().month-1)
        last_day_previous_month = calendar.monthrange(previous_month.year, previous_month.month)[1]
        # print(previous_month.month, date.today().month, last_day_previous_month)

        i = 0
        while day_order[0] != 'Monday':
            day_order.insert(0, calendar.day_name[previous_month.replace(day=last_day_previous_month-i).weekday()])
            day_numbers.insert(0, last_day_previous_month-i)
            month_number.insert(0, previous_month.month)
            i += 1
            dict_lenght += 1

    # print(current_day, month_lenght, current_day_name, first_day_name, month_lenght[1])
    return render_template('index.html', title='Login', day_order=day_order, day_numbers=day_numbers, month_number=month_number, dict_lenght=dict_lenght)
    




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
