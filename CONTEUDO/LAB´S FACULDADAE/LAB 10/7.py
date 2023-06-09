class Usuario:
	def __init__(self, primeiro_nome, ultimo_nome, idade):
		self.primeiro_nome = primeiro_nome
		self.ultimo_nome = ultimo_nome
		self.idade = idade
		
	def descreve_usuario(self):
		print('Primeiro nome: ' + self.primeiro_nome)
		print('Ultimo nome: ' + self.ultimo_nome)
		print('Idade: ' + str(self.idade))
		
	def comprimenta_usuario(self):
		print('Saudações ' + self.primeiro_nome + ', tudo bem com você?') 

class Admin(Usuario):
	def __init__(self, primeiro_nome, ultimo_nome, idade, previlegios = []):
		Usuario.__init__(self, primeiro_nome, ultimo_nome, idade)
		self.previlegios = previlegios
		
	def mostrar_previlegios(self):
		print('Previlegios:')
		for previlegio in self.previlegios:
			print('* ' + previlegio)
			
pessoa1 = Admin('José', 'Fonseca', 42, ['Pode adicionar postagem', 'Pode apagar postagem', 'Pode banir usuario'])
pessoa1.descreve_usuario()
pessoa1.mostrar_previlegios()
