class Privilegios:
	def __init__(self, privilegios = []):
		self.privilegios = privilegios
	
	def mostrar_privilegios(self):
		print('Privilegios:')
		print('')
		for privilegio in self.privilegios:
			print('* ' + privilegio + '.')

class Admin(Privilegios):
	def __init__(self, privilegios = []):
		Privilegios.__init__(self, privilegios)
		
