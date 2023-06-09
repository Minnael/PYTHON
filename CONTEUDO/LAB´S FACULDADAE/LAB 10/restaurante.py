class Restaurante:
	def __init__(self, nome, cozinha):
		self.nome = nome
		self.cozinha = cozinha
		
	def descreve_restaurante(self):
		print(self.nome, self.cozinha)
	
	def abre_restaurante(self):
		print('O restaurante foi aberto.')

