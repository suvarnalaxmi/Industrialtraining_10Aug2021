#read file using object
try:
    f=open("text.txt",'r',encoding='utf-8')
    print(f.read())
except:
     print("Not available")
finally:
    f=open("text.txt",'r',encoding="utf-8")
    f.close()