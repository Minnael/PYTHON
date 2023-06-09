pessoa_1 = {
	'Nome': 'Charles',
	'Sobrenome': 'Oliveira',
	'Idade': 32,
	'Cidade': 'Bronx',
}
pessoa_2 = {
	'Nome': 'João',
	'Sobrenome': 'Silva',
	'Idade': 27,
	'Cidade': 'São Paulo',
}

pessoa_3 = {
	'Nome': 'Gabriel',
	'Sobrenome': 'Pinto',
	'Idade': 41,
	'Cidade': 'Natal',
}

pessoas = [pessoa_1, pessoa_2, pessoa_3]

for pessoa in pessoas:
	for chave, valor in pessoa.items():
		print(chave +': '+ str(valor))
	print('\n')

