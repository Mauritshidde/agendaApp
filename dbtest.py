from flask_mysqldb import MySQL
import mysql.connector as mysql

import hashlib, string

from passwords import HOST, DATABASE, USER, PASSWORD

conn = mysql.connect(
   host=HOST, database=DATABASE, user=USER, password=PASSWORD
)
c = conn.cursor()

sql = "SELECT password FROM users WHERE username = %s"
val2 = ("eeeeeeee", )
c.execute(sql, val2)
storage = c.fetchall()
storage = storage[0][0]

salt = storage[:32]
hash = storage[32:]
print(salt, " jndajsda ", hash)

# salt = b'wL\xe3t\xd1\xae\x91I]\xfa\xd1\x8c~Z6\x88\x9a\xa9\x1dP\xd4\x9f"l\xb0~t\xaa2\xc4\xc5f'
# hash = b'\x8bz\xb22\xc5\x9d\x8c\xd5\xd1\xf6\x14:\x9f\xa1\x1c=\xb0\xaa\xcd\x94.\x86H\xe1\x10\xf8\xec&\xf0\x84B\x8a"|N!4\x17\r\x81n\xbb\xe9\xe1\x84\x91\xde1/\x85z\xc4\xa0\xde\xa1\xdd=\x99:l\xbb\xc9gZbx\x19\xa5Y!o\n3t\x98\xc3\xa4\xce!\xc8\x82\x99\x85z*\xd8V\x03\xbe\xa6Q\'\x90\xd0\xf0\x9ey\xfa\xa1o\xbe\x11"\x10\x85\xadT6N\xae$\xf6\xd6\x91]^\x8d\x9a\xf6\x80\xe3y\x85\x1a\x02\xba\xf6!'

# door = True
# password = 'l'

# list = string.printable
# for i in list:
#    password = i
#    new_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=128)    
#    print(i)
#    if hash == new_hash:
#       break

# print(password)
# c.execute(sql)


# conn.close()