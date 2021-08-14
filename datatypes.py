#Write a program to manipulate List data

A=['Apple','Banana','Custardapple','Jackfruit','Kiwi',11,12,13,14,15]
print("List A :",A[:])

print("List A : 2 to 5",A[2:6])

print("List A in reverse:",A[::-1])

A.append('fruits')
print("List A after appending  :",A[:])

A.insert(3,'Guava')
print("List A after inserting  :",A[:])

A.pop(1)
print("List A after poping :",A[:])

A.remove('Kiwi')
print("List A after removing :",A[:])

del A[0]
print("List A after deleteing :",A[:])

A.clear()
print("List A after clearing :",A[:])

#Write a program to manipulate Tuple data

B=("Apple","Banana","Custardapple","Guava","Jackfruit","Kiwi",11,12,13,14)

print("Tuple B:",B)

print("Tuple B: 2 to 5",B[2:6])

print("Tuple B in reverse:",B[::-1])

print("Count of Apple is :",B.count('Apple'))

print("Index of Apple",B.index('Apple'))
