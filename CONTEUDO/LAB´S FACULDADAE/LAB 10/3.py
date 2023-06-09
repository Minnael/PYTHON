class Usuario:
	def __init__(self, primeiro_nome, ultimo_nome, idade, altura, peso):
		self.primeiro_nome = primeiro_nome
		self.ultimo_nome = ultimo_nome
		self.idade = idade
		self.altura = altura
		self.peso = peso
		
	def descreve_usuario(self):
		print('Primeiro nome: ' + self.primeiro_nome)
		print('Ultimo nome: ' + self.ultimo_nome)
		print('Idade: ' + str(self.idade))
		print('Altura: ' + str(self.altura))
		print('Peso: ' + str(self.peso))
		
	def comprimenta_usuario(self):
		print('Saudações ' + self.primeiro_nome + ', tudo bem com você?') 

pessoa1 = Usuario('João', 'Silva', 37, 1.70, 72)
pessoa1.descreve_usuario()
pessoa1.comprimenta_usuario()

pessoa2 = Usuario('Maria', 'Fonseca', 22, 1.63, 52)
pessoa2.descreve_usuario()
pessoa2.comprimenta_usuario()
		
