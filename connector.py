# pip install mysql.connector

import mysql

from mysql import connector as c
from mysql.connector import Error



try:
    conn = c.connect(host="localhost",user="root",password="mohit@123")
    if conn.is_connected():
        cursor = conn.cursor()
        print("succesfully connected")
        
        # create a database
        cursor.execute("CREATE DATABASE flights;")
        conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)

#finally:
   # if conn.is_connected():
       # cursor.close()
       # conn.close()
    