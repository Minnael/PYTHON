convidados = ['Lucas', 'Kevin', 'Patolino']
	
print(convidados[2]+" não poderá comparecer ao jantar :(")
convidados[2] = "Mario"

for convidados in convidados:
	print("{}, você está sendo convidado para um jantar :)".format(convidados))

