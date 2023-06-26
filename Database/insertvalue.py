import os
os.system('cls')
import mysql.connector
try:
    db=mysql.connector.connect(host="localhost",user="root",passwd="",database="dbvit")
    if db.is_connected():
        print("Connected Scussfuly")
        objeCursor=db.cursor()
        sql = "INSERT INTO dbvit (NAME,BRANCH, ROLL,SECTION,AGE) VALUES (%s, %s,%s,%s,%s)"
        val = ("Shital", "MCA","1","A","22")
        objeCursor.execute(sql,val)
        db.commit()
    else:
        print("Not connexccted")
except Exception as e:
    print(e)
    