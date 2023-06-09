sanduiches = ['americano', 'pastrami', 'x-duplo', 'pastrami', 'x-tudo', 'pastrami']
prontos = []
x = str()
print('A lanchonete está sem sanduiches de pastrami.')

while 'pastrami' in sanduiches:
	sanduiches.remove('pastrami')

while sanduiches:
	x = sanduiches.pop()
	prontos.append(x)

print(prontos)

