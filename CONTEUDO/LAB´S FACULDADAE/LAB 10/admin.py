from privilegios import Privilegios

class Admin(Privilegios):
	def __init__(self, privilegios = []):
		Privilegios.__init__(self, privilegios)
