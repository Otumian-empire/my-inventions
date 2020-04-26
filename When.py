class When:
	def __init__(self, sample_arg, default_val = None):
		self.sample_arg = sample_arg
		self.default_val = default_val
		self.options = []

	def case(self, sample_case):
		self.options.append(sample_case)
		
	def default(self):
		if self.default_val != None:
			return self.default_val

	def run(self):
		for option in self.options:
			if self.sample_arg == option[0]:
				return option[1]
				
		self.default();

when = When(5)
when.case((1, "1"))
when.case((2,'2'))
when.case((3,'3'))
r = when.run()
print(r)
