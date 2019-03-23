largura = float(input("Largura da parade:"))
altura = float(input("Altura da parede:"))
area = largura * altura
tinta = area / 2
print("Sua parede tem dimensões de {}m x {}m, julgando pelos fatos sua área vai ser igual a {:.3f}.".format(largura, altura, area))
print("Para pintar sua parede você irá precisar de {}l de tinta.".format(tinta))
