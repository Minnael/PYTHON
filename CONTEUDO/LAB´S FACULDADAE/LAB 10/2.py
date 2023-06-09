class Restaurante:
	def __init__(self, nome, cozinha):
		self.nome = nome
		self.cozinha = cozinha
		
	def descreve_restaurante(self):
		print(self.nome, self.cozinha)
	
	def abre_restaurante(self):
		print('O restaurante foi aberto.')

restaurante1 = Restaurante('X', 'Y')
restaurante1.descreve_restaurante()

restaurante2 = Restaurante('I', 'J')
restaurante2.descreve_restaurante()

restaurante3 = Restaurante('K', 'Z')
restaurante3.descreve_restaurante()

