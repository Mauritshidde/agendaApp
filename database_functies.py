import os, hashlib, random, string
import mysql.connector as mysql

from flask import Flask, render_template, url_for, redirect, request, session, make_response

from passwords import HOST, PASSWORD, DATABASE, USER

    

def write_database(sql, value):
    conn = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )
    c = conn.cursor()
    c.execute(sql, value)

    conn.commit()
    conn.close()

def read_database(sql, value):
    conn = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )
    c = conn.cursor()
    c.execute(sql, value)

    data = c.fetchall()
    conn.close()

    if data == []:
        return "er zit niks in"
    else:
        return data[0]

def add_session_to_db(session_id, username):
    sql_r = "SELECT id FROM sessions WHERE sessionID = %s"
    value_r = (session_id, )
    data = read_database(sql_r, value_r)

    sql_u = "SELECT id FROM sessions WHERE username = %s"
    value_u = (username, )
    data_username = read_database(sql_u, value_u)

    if data == "er zit niks in" and data_username == "er zit niks in":
        sql = "INSERT INTO sessions (sessionID, username) VALUES (%s, %s)"
        val = (session_id, username, )
        write_database(sql, val)
        return True
    else:
        return False

def add_user(email, username, password):
    try:
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)
        storage = salt + key
        
        sql = "INSERT INTO users (email, username, password) VALUES (%s, %s, %s)"
        val = (email, username, storage, )

        write_database(sql, val)
        return True
    except:
        return False

def authenticate(username, password):
    
    sql = "SELECT password FROM users WHERE username = %s"
    val = (username, )
    
    storage = read_database(sql, val)
    storage = storage[0]
    
    salt_from_storage = storage[:32]
    key_from_storage = storage[32:]

    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt_from_storage, 100000, dklen=128)    

    if new_key == key_from_storage:
        return True
    else:
        return False

def authenticated(func):
    def wrapper():
        return func()
        try:
            if session['logged_in']:
                return func()
            else:
                return(redirect('signup'))
        except:
            return(redirect('signup'))
    return wrapper

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str