va = int(input("Qual a velocidade atural do carro?"))
vacm = (va - 80) * 7.00

if va <= 80:

    print("Tenha um bom dia! Dirija com segurança")

else:

    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h")
    print("Você deve pagar uma multa de R${:.2f}!" .format(vacm))
    print("Tenha um bom dia! Dirija com segurança")
