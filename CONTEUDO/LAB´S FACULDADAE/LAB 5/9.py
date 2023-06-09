import random
users = ['Carlos', 'Maria', 'Josefa', 'Antônio', 'admin']

random.shuffle(users)

for user in users:
	if user == 'admin':
		print('Olá admin, gostaria de ver um relatório de status?')
		
	else:
		print('Olá ' + user + ', obrigado por fazer login novamente.')
		
if len(users) == 0:
	print('Precisamos encontrar alguns usuários!')		

