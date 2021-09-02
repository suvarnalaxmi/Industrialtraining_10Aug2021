import MySQLdb
try:
    query="CREATE DATABASE EMPDB"
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="")
    cur=myconn.cursor()
    cur.execute(query)    
except:
    if myconn != None:
        myconn.rollback()
        print("Database connection has some issues")
finally:
    print("Cursor is closed")
    cur.close()
    myconn.close()
    print("Database connection is closed")
