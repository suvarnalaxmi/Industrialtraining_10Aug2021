import MySQLdb
try:
    query="create database studentdb"
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="")
    cur=myconn.cursor()
    print("execute cursor")
    cur.execute(query)    
    print("Execute query")
except:
    print("Database connection has some issues")
finally:
    cur.close()
    print("Cursor is closed")
    myconn.close()
    print("Database connection is closed")
