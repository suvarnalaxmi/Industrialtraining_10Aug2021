#if
print("if statement example")
a=20
n=int(input("Enter number: "))
if a>n:
    print(a,"is greater than",n)

#ifelse
print("ifelse statement example")
b=30
if b>n:
    print(b,"is greater than",n)
else:
    print(b,"is smaller than",n)

#elif
print("elif statement  example")
m=int(input("Enter number: "))
if m>0 :
    print(m,"is a positive number")
elif m==0:
        print("Number is zero")
else:
    print(m,"is a negative number")

#forloop
print("For  loop example")
list=[1,2,3,4,5,6,7,8,9]
sum=0
for num in list:
    sum=sum+num
    print("sum:",sum)

#whileloop
print("While loop example")
i = 1
while i < 6:
  print(i)
  i += 1

#Pass
print("Pass statement example")
if 10>5:
    pass

#break
print("Break statement example")
for s  in "training":
    if s=='i':
        break
    print(s)

#continue
print("Continue statement example")
for s  in "industrial training":
    if s=='i':
        continue
    print(s)