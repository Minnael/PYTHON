import random               # Também pode ser from random import randint

n1 = [0, 1, 2, 3, 4, 5]
n2 = random.choice(n1)      # Também pode ser n2 = randint(0, 5)

print("=-" * 40)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=" * 40)

np = int(input("Em que número você pensou?"))  # Jogador tentar adivinhar

print("PROCESSANDO...")

if np == n2:
    print("Parabéns! Você conseguiu me vencer!")
if np != n2:
    print("Ganhei eu pensei no número {} e não no {}!".format(n2, np))
if np > 5:
    print("Você digitou um número fora do combinado, por gentileza reinicie o game")




