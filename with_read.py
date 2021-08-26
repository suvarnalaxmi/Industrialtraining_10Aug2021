#using with to read from file
with open("text.txt",'r',encoding='utf-8') as f:
     print(f.read())
     f.close()