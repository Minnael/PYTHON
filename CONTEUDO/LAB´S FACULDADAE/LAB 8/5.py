while True:
	idade = int(input('Informe a sua idade: '))
	
	if idade < 3:
		print('Ingresso gratuito.')
	elif 3 <= idade <= 12:
		print('O ingresso custará 10 dólares.')
	else:
		print('O ingresso custará 15 dólares')
