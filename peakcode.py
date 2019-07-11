
def peak(mylist, mylistlen):
	for i in range(mylistlen):
		if mylist[i] >= mylist[i+1]:
			print(mylist[i], "is a peak at position", i)
		elif i == (mylistlen - 1) and mylist[i] >= mylist[i-1]:
			print(mylist[i], "is a peak at position", i)
		elif mylist[i] >= mylist[i+1] and mylist[i] >= mylist[i-1]:
			print(mylist[i], "is a peak at position", i)
		
				
x = [3, 2, 5, 4, 0, 1]
peak(x, 6)
print (5*"_$")

# y = [5, -7, 2, 4, 8, 0]
# peak(y, len(y))