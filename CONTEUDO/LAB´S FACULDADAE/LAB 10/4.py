class Restaurante:
	def __init__(self, nome, cozinha, numero_clientes):
		self.nome = nome
		self.cozinha = cozinha
		self.numero_clientes = 0
		
	def descreve_restaurante(self):
		print(self.nome, self.cozinha, self.numero_clientes)
	
	def abre_restaurante(self):
		print('O restaurante foi aberto.')
		
	def set_numero_clientes(self):
		self.numero_clientes = int(input())
	
restaurante = Restaurante('X', 'Y', '')
restaurante.descreve_restaurante()
restaurante.set_numero_clientes()
restaurante.descreve_restaurante()
