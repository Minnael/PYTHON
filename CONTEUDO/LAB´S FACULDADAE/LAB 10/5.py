class Usuario:
	def __init__(self, primeiro_nome, ultimo_nome, idade, altura, peso, tentativas_login):
		self.primeiro_nome = primeiro_nome
		self.ultimo_nome = ultimo_nome
		self.idade = idade
		self.altura = altura
		self.peso = peso
		self.tentativas_login = 0
		
	def descreve_usuario(self):
		print('Primeiro nome: ' + self.primeiro_nome)
		print('Ultimo nome: ' + self.ultimo_nome)
		print('Idade: ' + str(self.idade))
		print('Altura: ' + str(self.altura))
		print('Peso: ' + str(self.peso))
		print('Tentativas de login: ' + str(self.tentativas_login))
		
	def comprimenta_usuario(self):
		print('Saudações ' + self.primeiro_nome + ', tudo bem com você?') 

	def incrementa_tentativas_login(self):
		self.tentativas_login = self.tentativas_login + 1
		
	def reinicia_tentativas_login(self):
		 self.tentativas_login = 0
		
pessoa1 = Usuario('João', 'Silva', 37, 1.70, 72, '')

pessoa1.incrementa_tentativas_login()
pessoa1.incrementa_tentativas_login()
pessoa1.incrementa_tentativas_login()
pessoa1.incrementa_tentativas_login()

pessoa1.descreve_usuario()
pessoa1.comprimenta_usuario()

pessoa1.reinicia_tentativas_login()
pessoa1.descreve_usuario()

		

