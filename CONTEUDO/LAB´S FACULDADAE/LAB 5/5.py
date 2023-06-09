import random

cores = ['verde', 'amarelo', 'vermelho']
cor_alien = random.choice(cores)

if cor_alien == 'verde':
	print('O jogador acabou de ganhar +5 pontos')#verde

elif cor_alien == 'amarelo':
	print('O jogador acabou de ganhar +10 pontos')#amarelo

else:
	print('O jogador acabou de ganhar +15 pontos')#vermelho
	
