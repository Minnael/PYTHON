vc = float(input("Valor da casa: R$"))
sa = float(input("Salário do comprador: R$"))
fi = int(input("Quantos anos de financiamento?"))

pr = (vc) / (fi * 12)
tr = (sa * 30) / (100)

print("Para pegar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}." .format(vc, fi, pr))

if (pr > tr):
    print("Empréstimo NEGADO!")

elif (pr <= tr):
    print("Empréstimo pode ser CONCEDIDO!")


