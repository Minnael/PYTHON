convidados = ['Lucas', 'Kevin', 'Patolino']

print("Foram encontrados: Thiago, Kleber e Kleisson em uma mesa vizinha.")

convidados.insert(0, "Thiago")
convidados.insert(int((len(convidados))/2)+1, "Kleber")
convidados.append("Kleisson")

for x in range(len(convidados)):
	print("{}, você está sendo convidado para um jantar :)".format(convidados[x]))

print("Número de convidados: {}".format(len(convidados)))
