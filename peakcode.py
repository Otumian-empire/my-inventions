def peak(mylist, mylistlen):
	if not mylist or mylistlen == 0:
		print("There is no peak")
		return
		
	if mylistlen == 1:
		print(mylist[i], "is a peak at position", i)
		return
	for i in range(mylistlen - 1):

		if mylist[i] >= mylist[i + 1]:
			print(mylist[i], "is a peak at position", i)
		elif i == (mylistlen - 1) and mylist[i] >= mylist[i - 1]:
			print(mylist[i], "is a peak at position", i)
		elif mylist[i] >= mylist[i + 1] and mylist[i] >= mylist[i - 1]:
			print(mylist[i], "is a peak at position", i)
		
				
x = [3, 2, 5, 4, 0, 1]
peak(x, 6)
print(5 * "_$")

y = [5, -7, 2, 4, 8, 0]
peak(y, len(y))
