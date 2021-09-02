
import MySQLdb

try:
    query="delete from stdinfo  where name='Suvarnalaxmi'"
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("execute myconn")
    cur=myconn.cursor()
    print("execute cursor")
    cur.execute(query)
    print("execute query")
    myconn.commit()
    print("deleted row from table")
except:
    print("row not deleted")
    cur.close()
    print("close cursor")
    myconn.close()
    print("close myconn")
