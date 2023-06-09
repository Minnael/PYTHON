def faz_album(nome, album):
	cd = {
		'Nome': nome,
		'Album': album,
	}
	for x, y in cd.items():
		print(x + ': ' + str(y))

flag = True
while flag:
	nome = input()
	album = input()
	
	if nome == 'sair' or album == 'sair':
		flag = False
	
	else:
		faz_album(nome, album)
	
