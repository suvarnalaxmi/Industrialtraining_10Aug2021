alist = ["abc", "def", "ghi", "jkl"]
indices = [0, 1, "2", 3]
for i in range(len(indices)):
	try:
		print(alist[indices[i]])
	except TypeError:
		print("TypeError: Check list of indices")

