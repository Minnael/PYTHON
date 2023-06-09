from collections import OrderedDict
palavras = OrderedDict()

palavras['Tupla'] = 'Tupla é uma estrutura de dados similar a uma lista, porém imutável.'
palavras['If'] = 'O If é usado como "se", ou seja, se algo acontecer execute o que está dentro do if.'
palavras['For'] = 'O for é um laço de repetição que repete em função dos parametros fornecidos.'
palavras['Dicionário'] = 'Um dicionário é uma estrutura de dados do tipo coleção. Portanto contém mais de um valor.'
palavras['Python'] = 'Python é uma linguagem de programação que permite fazer coisas incríveis em muito pouco tempo de aprendizado.'
palavras['Variavéis'] = 'Valores que são manipulados com foco na resolução de um problema.'
palavras['Str'] = 'Str representa valores do tipo string.'
palavras['Int'] = 'Int representa valores do tipo inteiro.'
palavras['Print'] = 'Responsável por exibir uma mensagem na tela.'

for name, palavra in palavras.items():
	print(name.title() + ': ' + palavra)
