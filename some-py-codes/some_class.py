class X:
	count = 0

	def __init__(self, y):
		self.y = self.check_y(y)
		X.count += 1

	def get_y(self):
		return self.y

	@classmethod
	def get_c(cls):
		return cls.count

	@staticmethod
	def  check_y(y):
		if y % 2 == 1:
			y = 0
		return y

a = X(1)
b = X(2)
c = X(3)

for i in a, b, c:
	print("value of object - ", i.get_y())
	print("count - ", i.get_c())

print()
print(X.get_c())
print(a.check_y(1))

