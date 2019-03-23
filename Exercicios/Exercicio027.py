nome = str(input("Qual é o seu nome completo ?")).strip()
n1 = nome.split()

print("Muito prazer em conhcer!")
print("Seu primeiro nome é {}" .format(n1[0]))
print("Seu último nome é {}" .format(n1[len(n1)-1]))
