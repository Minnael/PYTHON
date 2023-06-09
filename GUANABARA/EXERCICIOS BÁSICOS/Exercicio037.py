import colorize

numero = int(input("Digite um número inteiro:"))

print("Escolha uma das bases para conversão:")
print("\033[1;33m [ 1 ] converter para BINÁRIO")
print("\033[1;33m [ 2 ] converter para OCTAL")
print("\033[1;33m [ 3 ] converter para HEXADECIMAL")

escolha = int(input("Sua opção:"))

if escolha == 1:
    print("{} convertido para BINÁRIO é igual a {}" .format(numero, bin(numero)[2:]))
elif escolha == 2:
    print("{} convertido para OCTAL é igual a {}" .format(numero, oct(numero)[2:]))
elif escolha == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(numero, hex(numero)[2:]))


