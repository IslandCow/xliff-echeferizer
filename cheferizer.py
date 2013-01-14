import string

class EChef:
	def A(token):
		return 'x'

	def B(token):
		return 'q'

	rules = {'a': A, 'b': B}

	def isUpper(self, token):
		if token in string.uppercase:
			return True
		else:
			return False

	def transform(self, token):
		upper = self.isUpper(token)
		x = self.rules[token.lower()](token)
		if upper:
			return x.upper()
		else:
			return x.lower()

e = EChef()
testString = "a"
bigString = "B"
print e.transform(testString)
print e.transform(bigString)
