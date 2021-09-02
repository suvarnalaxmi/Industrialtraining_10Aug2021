import MySQLdb

try:
    query="""insert into stdinfo values('Suvarnalaxmi','Solapur','Solapur city')"""
    
    myconn=MySQLdb.connect(host="localhost",user="root",passwd="",database="studentdb")
    print("execute myconn")
    cur=myconn.cursor()
    print("execute cursor")
    cur.execute(query)
    print("execute query")
    myconn.commit()
    print("inserted value into table")
except:
    print("values not inserted")
finally:
    cur.close()
    print("close cursor")
    myconn.close()
    print("close myconn")
