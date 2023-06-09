nomecomp = str(input("Digite seu nome completo aqui :"))
primenome = nomecomp.split()

print("Aguarde, estamos analisando o seu nome...")

print("Seu nome em letras maiúsculas é {}" .format(nomecomp.upper()))

print("Seu nome em letras minúsculas é {}" .format(nomecomp.lower()))

print("Seu nome ao todo possui {} letras" .format(len(nomecomp)))

print("Seu primeiro nome é {} e ele possui um total de {} letras " .format(primenome[0], len(primenome[0])))

