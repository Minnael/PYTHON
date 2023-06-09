itens = ['Cebola', 'Tomate', 'Carne']

def sanduiche(*x):
	print('O sanduiche contém os seguintes itens: ' + str(x))
	
	
for iten in itens:
	sanduiche(iten)
