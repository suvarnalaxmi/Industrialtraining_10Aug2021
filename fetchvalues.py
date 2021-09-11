import MySQLdb

try:
    query="select * from stdinfo"
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    cur=myconn.cursor()
    print("myconn excecute")
    cur.execute(query)
    print("execute query")
    myconn.commit()

    tdata=cur.fetchall()
    print("Records are ")
    for row in tdata:
        print("name       : ",row[0])
        print("birthplace : ",row[1])
        print("address    : ",row[2])

    print("values fetched")
except:
    print("values not fetched...")
finally:
    cur.close()
    print("close cursor")
    myconn.close()
    print("close myconn")