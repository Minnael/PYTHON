from random import randint 

class Dado:
	def __init__(self, lados=6):
		self.lados = lados
	
	def jogar_dado(self):
		lado = randint(1, 6)
		print(lado)

dado = Dado('')
for i in range(0, 10):
	dado.jogar_dado()
		
		
