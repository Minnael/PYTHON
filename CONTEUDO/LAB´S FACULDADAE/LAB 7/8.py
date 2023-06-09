gato = {
	'Animal': 'Gato',
	'Dono': 'Darlene',
}

cachorro = {
	'Animal': 'Cachorro',
	'Dono': 'Jorge',
}

coelho = {
	'Animal': 'Coelho',
	'Dono': 'Bia',
}

pets = [gato, cachorro, coelho]

for pet in pets:
	for chave, valor in pet.items():
		print(chave + ': ' + valor)
		
	print('\n')
