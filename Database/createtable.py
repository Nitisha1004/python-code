import os
os.system('cls')
import mysql.connector
try:
    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="dbvit")
    if db.is_connected():
        print("Connected Scussfuly")
        objeCursor=db.cursor()
        student="""CREATE TABLE dbvit (
                   NAME  VARCHAR(20) NOT NULL,
                   BRANCH VARCHAR(50),
                   ROLL INT NOT NULL,
                   SECTION VARCHAR(5),
                   AGE INT
                   )"""
        objeCursor.execute(student)
        db.close()
    else:
        print("Not connexccted")
except Exception as e:
    print(e)
    