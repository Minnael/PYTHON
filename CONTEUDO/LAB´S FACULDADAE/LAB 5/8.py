import random
users = ['Carlos', 'Josefa', 'Antônio', 'Maria', 'admin']

random.shuffle(users)

for user in users:
	if user != 'admin':
		print('Olá ' + user + ', obrigado por fazer login novamente.')
		
	else:
		print('Olá admin, gostaria de ver um relatório de status?')
