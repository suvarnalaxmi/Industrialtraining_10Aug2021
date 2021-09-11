import MySQLdb
try:
    query="CREATE DATABASE EMPDB"
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="")
    cur=myconn.cursor()
    print("cursor connection established succesfully")
    cur.execute(query)  
    print("Query executed")  
except:
    if myconn != None:
        myconn.rollback()
        print("Database connection has some issues")
finally:
    cur.close()
    print("Cursor is closed")
    myconn.close()
    print("Database connection is closed")
