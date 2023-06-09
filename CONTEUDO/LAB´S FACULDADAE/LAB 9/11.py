magicos = ['Houdini', 'Fu-Manchu', 'Richiardi Jr', 'Jasper Maskelyne']
copia = magicos.copy()
grande = ''

def torna_grandioso():
	c = 0
	for cop in copia:
		grande = 'o Grande ' + cop
		del(copia[c])
		copia.insert(c, grande)
		
		grande = ''
		c = c + 1
		
torna_grandioso()
	
def mostra_magicos(x):
	for magico in x:
		print(magico)

mostra_magicos(magicos)
mostra_magicos(copia)

	


