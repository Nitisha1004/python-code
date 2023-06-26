# pip install mysql-connector-python
# import MySql
# connect()  method
# cursor() method
# execute()
# fetchall()
# fetchmany()
# cursor()
# connection.close()

# 
import  os
os.system('cls')
# Create a database
import mysql.connector
try:
    db=mysql.connector.connect(host="localhost",port = "3306", user="root",passwd="")
    if db.is_connected():
        print("Connected Scussfuly")
        strQuery="Create  DATABASE dbvit1"
        objeCursor=db.cursor()
        objeCursor.execute(strQuery)
        db.close()
    else:
        print("Not connexccted")
except Exception as e:
    print(e)
    