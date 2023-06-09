peso = int(input("Qual a sua massa corporal(kg)?"))
altura = float(input("Qual a sua altura(m)?"))
imc = peso / (altura * altura)

print("Seu IMC é {:.2f}" .format(imc))

if (imc < 18.5):

    print("Você está ABAXIO do peso.")
    print("Como mais proteínas e carboidratos.")

elif (imc >= 18.5 and imc < 25):

    print("Você está com o PESO IDEAL.")
    print("Parabéns, continue assim.")

elif (imc >= 25 and imc < 30):

    print("Você está SOBREPESO.")
    print("Tente diminuir as calorias em suas refeições.")

elif (imc >= 30 and imc <= 40):

    print("Você está com OBESIDADE.")
    print("Tente fazer refeições com uma menos quantidade de calorias")

elif (imc > 40):

    print("ATENÇÂO")
    print("Você está com OBESIDADE MÓRBIDA")
    print("Vá ao médico urgentemente e se possível faça uma acompanhamento semanalamente.")