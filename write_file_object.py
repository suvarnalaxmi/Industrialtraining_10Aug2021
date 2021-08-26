#write file using object
try:
    f=open("text.txt",'w',encoding="utf-8")

    f.write("Using Object method ")
except:
    print("Not available")
finally:
     f=open("text.txt",'w',encoding="utf-8")
     f.close()