print("=" * 10, "LOJAS PATOLINO", "=" * 10)

preço = int(input("Preço das comprar: R$"))
vistasc = preço - ((preço * 10) / 100)
vistacc = preço - ((preço * 5) / 100)
x1 = (preço / 2)

print("FORMAS DE PAGAMENTO")

print("[ 1 ] à vista dinheiro/cheque.")
print("[ 2 ] à vista no cartão.")
print("[ 3 ] 2x no cartão.")
print("[ 4 ] 3x ou mais no cartão.")

opção = int(input("Qual é a sua opção?"))

if (opção == 4):

    parcelas = int(input("Com quantas parcelas pretende pagar?"))
    x2 = (preço / parcelas)
    preçofinal = preço + ((preço * 20) / 100)

    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS" .format(parcelas, x2))
    print("Sua compra de {:.2f} vai custar R${:.2f} no final." .format(preço, preçofinal))

elif (opção == 3):

    print("Sua compra de {:.2f} R$ será dividida em 2x" .format(preço))
    print("Suas parcelas serão de {:.2f} R$" .format(x1))

elif (opção == 2):

    print("Como vai pagar a vista no cartão sua compra terá um desconto de 5%")
    print("Sendo assim a compra que era de {:.2f} R$ será agora de {:.2f} R$" .format(preço, vistacc))

elif (opção == 1):

    print("Como vai pagar a vista á dinheiro/cheque você terá um desconto de 10%")
    print("Sendo assim a comrpa que era de {:.2f} R$ será gora de {:.2f} R$" .format(preço, vistasc))

