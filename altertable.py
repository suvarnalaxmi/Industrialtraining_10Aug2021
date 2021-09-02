import MySQLdb

try:
    query="alter table stdinfo add emailid varchar(50)"
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("execute myconn")
    cur=myconn.cursor()
    print("execute cursor")
    cur.execute(query)
    print("execute query")
    myconn.commit()
    print("altered table table")
except:
    print("values not altered")
    cur.close()
    print("close cursor")
    myconn.close()
    print("close myconn")
