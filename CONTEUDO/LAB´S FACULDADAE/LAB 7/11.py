cidades = {
	'Santa Cruz': {
		'Pais': 'Brasil',
		'Populacao': 40295,
		'Fatos': 'Estátua de Santa Rita de Cássia',
	},
	'Mossoró': {
		'Pais': 'Brasil',
		'Populacao': 300618,
		'Fatos': 'Calor',
	},
	'Tangará': {
		'Pais': 'Brasil',
		'Populacao': 15869,
		'Fatos': 'Pastel',
	},
}

for cidade, dados in cidades.items():
	print(cidade)
	for chave, valor in dados.items():
		print(chave +': '+ str(valor))
	print('\n')

