import random

class Ajuste():
	def __init__(self):
		self.possibilidades = [[260, 130], [310, 180], [360, 230], [410, 280], [450, 320]]
		self.possibilidade = random.randint(0, 4)
	
	def altura(self):
		return self.possibilidades[self.possibilidade]

ajuste = Ajuste()
print(ajuste.altura()[0])
