from flask_mysqldb import MySQL
import mysql.connector as mysql

from passwords import HOST, DATABASE, USER, PASSWORD

conn = mysql.connect(
   host=HOST, database=DATABASE, user=USER, password=PASSWORD
)
c = conn.cursor()

delete = '''DROP TABLE users'''
delete2 = '''DROP TABLE dailyTasks'''

users = '''CREATE TABLE users(
   id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   email CHAR(100) NOT NULL UNIQUE,
   username CHAR(100) NOT NULL UNIQUE,
   password TINYBLOB
)'''

daily_Tasks = '''CREATE TABLE dailyTasks(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    userID INT NOT NULL,
    day INT NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL,
    title TEXT NOT NULL,
    text TEXT NOT NULL
)'''

c.execute(delete)
c.execute(delete2)
c.execute(users)
c.execute(daily_Tasks)

conn.close()