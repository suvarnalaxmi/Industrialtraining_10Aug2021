
import MySQLdb

try:
    query="drop table stdinfo"
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("execute myconn")
    cur=myconn.cursor()
    print("execute cursor")
    cur.execute(query)
    print("execute query")
    myconn.commit()
    print("deleted table")
except:
    print("not deleted")
    cur.close()
    print("close cursor")
    myconn.close()
    print("close myconn")
