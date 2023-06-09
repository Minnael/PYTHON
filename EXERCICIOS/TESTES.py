class Biblioteca():
	def __init__(self, nome):
		self.nome = nome
		self.catalago = {}
	
	def add_livro(self, nome_livro):
		self.catalago[nome_livro] = 1
		print(f'{nome_livro} adicionado ao catálago')
	
	def empresta_livro(self, nome_livro):
		if nome_livro in self.catalago.keys() and self.catalago[nome_livro] == 1:
			self.catalago[nome_livro] = 0
			print(f'{nome_livro} emprestado')
		elif nome_livro not in self.catalago.keys():
			print(f'{nome_livro} não está no catálogo')
		else:
			print(f'{nome_livro} já foi emprestado')
		
	def lista_catalogo(self):
		print(self.nome)
		for k, v in self.catalago.items():
			if v == 1:
				print(f'{k} (disponível)')
			else:
				print(f'{k} (emprestado)')

my_biblioteca = Biblioteca(input())
n = int(input())

for i in range(n):
	evento = input().split()
	if evento[0] == 'adicionar':
		my_biblioteca.add_livro(evento[1])
	elif evento[0] == 'emprestar':
		my_biblioteca.empresta_livro(evento[1])
	else:
		my_biblioteca.lista_catalago()
