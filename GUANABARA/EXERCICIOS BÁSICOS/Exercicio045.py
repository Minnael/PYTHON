import random
import time

lista = [1, 2, 3]
pc = random.choice(lista)

print("Suas opções:")

print("[ 1 ] PEDRA")
print("[ 2 ] PAPEL")
print("[ 3 ] TESOURA")

opção = int(input("Qual vai ser a sua jogada?"))

time.sleep(1)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO")
time.sleep(1)

print("=-=" * 10)

if (opção == 1 and pc == 1):

    print("Computador jogou Pedra")
    print("Jogador jogou Pedra")
    print("=-=" * 10)
    print("Temos um EMPATE")

elif (opção == 2 and pc == 2):

    print("Computador jogou Papel")
    print("Jogador jogou Papel")
    print("=-= " * 10)
    print("Temos um EMPATE")

elif (opção == 3 and pc == 3):

    print("Computador jogou Tesoura")
    print("Jogador jogou Tesoura")
    print("=-=" * 10)
    print("Temos um EMPATE")

elif (opção == 1 and pc == 2):

    print("Computador jogou Papel")
    print("Jogaddor jogou Pedra")
    print("=-=" * 10)
    print("Computador VENCEU!")

elif (opção == 2 and pc == 3):

    print("Computador jogou Tesoura")
    print("Jogador jogou Papel")
    print("=-=" * 10)
    print("Computador VENCEU!")

elif (opção == 3 and pc == 1):

    print("Computador jogou Pedra")
    print("Jogador jogou Tesoura")
    print("=-=" * 10)
    print("Computador VENCEU!")

elif (opção == 2 and pc == 1):

    print("Computador jogou Pedra")
    print("Jogador jogou Papel")
    print("=-=" * 10)
    print("Jogador VENCEU!")

elif (opção == 3 and pc == 2):

     print("Computador jogou Papel")
     print("Jogador jogou Tesoura")
     print("=-=" * 10)
     print("Jogador VENCEU!")

elif (opção == 1 and pc == 3):

    print("Computador jogou Tesoura")
    print("Jogador jogou Pedra")
    print("=-=" * 10)
    print("Jogador VENCEU!")
