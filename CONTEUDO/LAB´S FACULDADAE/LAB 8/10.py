lugares = []
ativo = True

while ativo:
	lugar = input('Se pudesse visitar um lugar do mundo, para onde você iria? ')
	lugares.append(lugar)
	
	repetir = input('Alguém mais gostaria de participar da enquete? (sim/nao) ')
	if repetir == 'nao':
		ativo = False

for lugar in lugares:
	print(lugar + ': ' + str(lugares.count(lugar)))
	y = lugares.count(lugar)
	
	for x in range(0, y-1):
		lugares.remove(lugar)
	
	y = 0
		
		
