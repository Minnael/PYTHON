d = float(input("Qual a distância da viagem?"))

if (d <= 200) :

    print("Você está prestes a começar uma de viagem de {}Km" .format(d))
    print("E o preço da sua passagem será de R${:.2f}" .format(d * 0.50))

else:

    print("Você está prestes a começar uma viagem de {}" .format(d))
    print("E o preço da sua passagem será de R${:.2f}" .format(d * 0.45))