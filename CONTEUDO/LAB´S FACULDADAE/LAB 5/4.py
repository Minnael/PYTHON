import random

cores = ['verde', 'amarelo', 'azul', 'vermelho']
cor_alien = random.choice(cores)

if cor_alien == 'verde': 
	print('O jogador acabou de ganhar +5 pontos')

else:
	print('O jogador acabou de ganhar +10 pontos')	
