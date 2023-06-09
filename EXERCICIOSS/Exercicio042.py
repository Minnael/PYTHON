print("-=-" * 10)
print("Analisador de Triângulos")
print("-=-" * 10)

r1 = float(input("Primeiro segmento:"))
r2 = float(input("Segundo segmento:"))
r3 = float(input("Terceiro segmento:"))


if (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 and r2 == r3):

    print("Os segmentos acima podem formar um triângulo, sendo ele EQUILÁTERO!")

elif (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 != r3 or r1 == r3 != r2 or r3 == r2 != r1):

    print("Os segmentos acima podem formar um triângulo, sendo ele ISÓSCELES!")

elif (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 != r2 != r3 != r1):

    print("Os segmentos acima podem formar um triângulo, sendo ele ESCALENO!")

else:
    print("Os segmentos acima não podem formar triângulo")

