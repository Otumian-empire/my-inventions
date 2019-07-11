# my mysquareroot.py
# a program that computes the square root of a number

for i in range(0, 50):
	for x in range(1, i):
		if i / x == x:
			print("the square root of {} is {}".format(i, x))