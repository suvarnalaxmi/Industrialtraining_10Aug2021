#using with to write
with open ("text.txt",'w',encoding='utf-8') as f:
    f.write("Using with to write into file")
    f.close()