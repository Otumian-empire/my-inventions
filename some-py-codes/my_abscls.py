import abc


class AbstractClass:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def set_val(self, input):
		return 

	@abc.abstractmethod
	def get_val(self):
		return 


class MyClass(AbstractClass):

	def set_val(self, input):
		self.input = input

	def get_val(self):
		return self.input


m = MyClass()
m.set_val(23)
print(f"The value is {m.get_val()}")

