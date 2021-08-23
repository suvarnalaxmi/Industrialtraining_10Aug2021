#value error
def fun():
    x = int("four")

try:
    fun()
except ValueError as e:
    print("Value Error :- ", e)



    
