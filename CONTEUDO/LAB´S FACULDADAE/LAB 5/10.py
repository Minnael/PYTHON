users_atuais = ['um', 'dois', 'três', 'quatro', 'cinco']
users_novos = ['quatro', 'cinco', 'seis', 'sete', 'oito']

for novos in users_novos:
	
	for atuais in users_atuais:
		
		if novos.upper() == atuais.upper():
			print('*Forneça um novo nome.*')
			
		else:
			print('Este nome de usuário está disponível.')
			
		
