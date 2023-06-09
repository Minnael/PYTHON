magicos = ['Houdini', 'Fu-Manchu', 'Richiardi Jr', 'Jasper Maskelyne']
grande = ''

def torna_grandioso():
	c = 0
	for magico in magicos:
		grande = 'o Grande ' + magico 
		del(magicos[c])
		magicos.insert(c, grande)
		
		grande = ''
		c = c + 1
		
torna_grandioso()
	
def mostra_magicos():
	for magico in magicos:
		print(magico)

mostra_magicos()

	

