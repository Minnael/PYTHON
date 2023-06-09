import random

name1 = str(input("Primeiro aluno:"))
name2 = str(input("Segundo aluno:"))
name3 = str(input("Terceiro aluno:"))
name4 = str(input("Quarto aluno:"))

lista = [name1, name2, name3, name4]

n1 = random.choice(lista)

print("O aluno que vai limpar o quadro hoje é {}".format(n1))