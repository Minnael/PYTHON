preço = float(input("Qual é o preço do produto? R$"))
desconto = preço * 5 / 100
pfinal = preço - desconto
print("O produto que custava R${}, na promoção com 5% de desconto vai custar R${:.2f}".format(preço, pfinal))