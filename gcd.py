# gcd.py

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)


def lcm(a, b):
	return (a * b) / gcd(a, b)


a = 24
b = 18
	
print('the gcd of', a, 'and', b, 'is', gcd(a, b))

print('the lcm of', a, 'and', b, 'is', lcm(a, b))