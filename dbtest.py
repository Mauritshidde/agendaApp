from flask_mysqldb import MySQL
import mysql.connector as mysql

from passwords import HOST, DATABASE, USER, PASSWORD

conn = mysql.connect(
   host=HOST, database=DATABASE, user=USER, password=PASSWORD
)
c = conn.cursor()

sql = "SELECT * FROM users WHERE id = %s"
val2 = ("; update users set password = 'true' where id = '1';", )
c.execute(sql, val2)
print(c.fetchall())
c.execute(sql)

conn.close()