def faz_album(nome, album, faixas):
	cd = {
		'Nome': nome,
		'Album': album,
		'Faixas': faixas,
	}
	for x, y in cd.items():
		print(x + ': ' + str(y))
	
faz_album('João', 'X', 20)
faz_album('Maria', 'Y', 30)
faz_album('Caros', 'z', 11)
