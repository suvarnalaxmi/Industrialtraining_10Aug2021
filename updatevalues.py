import MySQLdb

try:
    query="update  stdinfo set address='pune' where name='Suvarnalaxmi'"
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("execute myconn")
    cur=myconn.cursor()
    print("execute cursor")
    cur.execute(query)
    print("execute query")
    myconn.commit()
    print("updated value into table")
except:
    print("values not updated")
finally:
    cur.close()
    print("close cursor")
    myconn.close()
    print("close myconn")
