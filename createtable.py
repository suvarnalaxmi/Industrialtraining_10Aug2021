import MySQLdb

try:
    query="create table stdinfo(name varchar(50),birthplace varchar(40),address varchar(40))"
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("execute myconn")
    cur=myconn.cursor()
    print("execute cursor")
    cur.execute(query)
    print("execute query")
    print("table created")
except:
    print("table not created")
finally:
    cur.close()
    print("close cursor")
    myconn.close()
    print("close myconn")
