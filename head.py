class Head:

	def __init__(self, value):
		self.value = value

	def __eq__(self, other):
		#print (self.value, other)

		# Verifica se o primeiro valor é um tipo primitivo (int, str, bool)
		if isinstance (self.value, type):
			# Verifica se o segundo valor é um tipo primitivo (int, str, bool)
			if isinstance(other, type):
				# Caso ambos sejam tipos primitivos retorna falso
				# ex: (str, int)
				return False
			# Caso o segundo seja um valor normal compara com o tipo
			# ex: (bool, True)
			return isinstance(other, self.value)
		# Se o primeiro valor não for um tipo primitivo
		# ou seja, um valor normal, como: 12, 'maria', 45.7
		else:
			# Se o segundo valor for um tipo primitivo usa o isinstance
			# ex: (12, int)
			if isinstance(other, type):
				return isinstance(self.value, other)
			# Se o segundo valor for um valor normal compara o tipo dos dois
			# ex: (12, 15)
			else:
				return type(self.value) == type(other)
			
		return False

	def __str__(self):
		return str(self.value)
