class Usuario:
	def __init__(self, primeiro_nome, ultimo_nome):
		self.primeiro_nome = primeiro_nome
		self.ultimo_nome = ultimo_nome
	
	def descreve_usuario(self):
		print(f'Primeiro nome do usuário: {self.primeiro_nome}')
		print(f'Ultimo nome do usuário: {self.ultimo_nome}')
	
	def comprimenta_usuario(self):
		print(f'Olá {self.primeiro_nome} {self.ultimo_nome}')
	
user1 = Usuario('Jose', 'Silva')
user1.descreve_usuario()
user1.comprimenta_usuario()
