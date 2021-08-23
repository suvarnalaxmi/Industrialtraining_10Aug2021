x = 5
try:
    def printx():
         print(x)
         x = x + 1
    printx()
except:
    print("This is unbound local error")
