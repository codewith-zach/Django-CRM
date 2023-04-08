# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='playboy@123'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE crm_tut")

print("All Done!")
