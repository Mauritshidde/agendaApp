import os, hashlib
import mysql.connector as mysql

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
    
    return data[0]

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