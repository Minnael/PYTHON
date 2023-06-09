import random
idades = list(range(1,67))
idade = random.choice(idades)
print('A idade escolhida foi: '+str(idade))

if idade < 2:
	print('Você é um bebê.')
	
elif idade >= 2 and idade < 4:
	print('Você é uma criança.')
	
elif idade >= 4 and idade < 13:
	print('Você é um garoto ou garota.')
	
elif idade >= 13 and idade < 20:
	print('Você é um(a) adolescente.')
	
elif idade >= 20 and idade < 65:
	print('Você é um adulto.')
	
else:
	print('Você é um idoso')
