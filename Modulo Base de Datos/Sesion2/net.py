#pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventario"
)

mycursor = mydb.cursor(dictionary=True)