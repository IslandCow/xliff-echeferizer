import string

class EChef:
	def isUpper(self, token):	
		if token.islower():
			return "lower"
		elif token.isupper(): 
			return "upper"
		else:
			return "capitalize"

	numCharacters = 0	

	def X(self, string):
		casing = self.isUpper(string)
		s = self.Z(string.lower())
		func = getattr(s,casing)
		return func()
		
	def Z(self, string):
		c = ''
		if len(string) == 0:
			return c
		else:
			c = string[0]

		resultString = ""
		self.numCharacters += 1
		res = ""
		if c in self.rules:
			x = self.rules[c]
			resultString+=(x(self, string))
		else:
			resultString+=(c)
			resultString+=(self.Z(string[1:]))

		return resultString 

	iReplaced = False

	def repl(self, token, replacements, finish):
		string = ""
		remainder = token
		replaced = False
		for st, value in replacements.items():
			classlen = len(st)
			if token[:classlen] == st:
				replaced = True
				string = value
				remainder = token[classlen:]
				break
		if not replaced:
			string, remainder = finish(string, token)
		return string + self.Z(remainder)

	def fin(self, string, token):
		string = token[0]
		remainder = token[1:]	
		return string, remainder

	def O(self, token):
		reps = {"ow": "oo", "o": "u"}
		return self.repl(token, reps, self.fin)
	
	def iFin(self, string, token):
		remainder = token[1:]
		string = "i"
		if not self.iReplaced:
			if self.numCharacters > 1:
				self.iReplaced = True
				string = "ee"
		return string, remainder

	def I(self, token):
		reps = {"ir": "ur"}
		return self.repl(token, reps, self.iFin)

	def aFin(self, string, token):
		if len(token) <= 1:
			string = "a"
		else:
			string = "e"
		remainder = token[1:]	
		return string, remainder

	def A(self, token):
		replacements = {"an": "un", "au": "oo"}
		return self.repl(token, replacements, self.aFin)

	def W(self, token):
		reps = {"w": "v"}
		return self.repl(token, reps, self.fin)

	def V(self, token):
		reps = {"v": "f"}
		return self.repl(token, reps, self.fin)

	def T(self, string):
		reps = {"tion": "shun", "the": "zee"}
		return self.repl(string, reps, self.fin)

	def E(self, token):
		replaced = False
		reps = {"en": "ee", "e": "e-a"}
		for st, value in reps.items():
			classlen = len(st)
			if token[:classlen] == st:
				if classlen == len(token):
					replaced = True
					string = value
					remainder = token[classlen:]
					break
		if not replaced:
			string = "e"
			remainder = token[1:]
		return string + self.Z(remainder)

	def F(self, token):
		reps = {"f": "ff"}
		return self.repl(token, reps, self.fin)

	rules = {'a': A, 'f': F, 't': T, 'i': I, 'o': O, 'w': W, "v": V, "e": E}

	def parse(self, string):
		return self.X(string)


