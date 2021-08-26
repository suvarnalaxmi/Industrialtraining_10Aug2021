import os

print("Current directory::"+os.getcwd())

filename = 'D:/python/IT/Industrialtraining_10Aug2021/testing.txt'

print("Size :: "+str(os.path.getsize(filename)))
print("Last modified date :: "+str(os.path.getmtime(filename)))
print("Creation date and time ::"+str(os.path.getctime(filename)))