class Restaurante:
	def __init__(self, nome, cozinha):
		self.nome = nome
		self.cozinha = cozinha
		
	def descreve_restaurante(self):
		print(self.nome, self.cozinha)
	
	def abre_restaurante(self):
		print('O restaurante foi aberto.')

class Sorveteria(Restaurante):
	def __init__(self, nome, cozinha, sabores = []):
		Restaurante.__init__(self, nome, cozinha)
		self.sabores = sabores
		
	def mostrar_sabores(self):
		print(self.sabores)

restaurante1 = Restaurante('X', 'Y')
restaurante1.descreve_restaurante()
sorveteria1 = Sorveteria('I', 'J', ['Chocolate', 'Baunilha', 'Morango', 'Napolitano'])
sorveteria1.descreve_restaurante()
sorveteria1.mostrar_sabores()

