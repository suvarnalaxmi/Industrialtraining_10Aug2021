#overflow 
i=1
try:
    f = 3.0**i
    for i in range(100):
        print( i, f)
        f = f ** 2
except OverflowError as err:
    print ("Overflowed after ", f, err)