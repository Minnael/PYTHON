favorite_languages = {
	'jen': ['python', 'ruby'],  
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	'Karen': [],
	'Caio': [], 
	'Julio': [],
}

for name, languages in favorite_languages.items(): 
	if len(languages) > 0:
		print('\n' + name + ' muito obrigado por ter participado da enquete.')
	else:
		print('\n' + name + ' percebi que você ainda não participou da enquete, te convido a participar.')
