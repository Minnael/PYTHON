string = 'string'
print(string == 'string')
print(string != 'string')

print(5*"=")

lower = 'LOWER'
print(lower.lower() == 'lower')
print(lower.lower() == lower)

print(5*"=")

idade = 18
print(idade == 18)
print(idade != 17)
print(idade > 17)
print(idade >= 17)
print(idade != 18)
print(idade == 17)
print(idade < 17)
print(idade <= 17)

print(5*"=")

velocidade_0 = 100
velocidade_1 = 120
print(velocidade_0 >= 100 and velocidade_1 <= 120)
print((velocidade_0 + velocidade_1) == 220 or velocidade_0 < 0)
print(velocidade_0 >= 90 and velocidade_1 >= 130)
print(velocidade_1 <= 110 or velocidade_0 >= 110)

print(5*"=")

lista = list(range(1, 11))
print(1 in lista)
print(11 in lista)

print(5*"=")

x = int(17)
if x not in lista:
	print(str(x) + ' não está na lista')  

















