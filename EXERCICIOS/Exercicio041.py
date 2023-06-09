import datetime

nascido = int(input("\033[1;32;41mAno em que nasceu:\033[m"))
atual = datetime.date.today().year
anos = atual - nascido

print("\033[1;31;42mO atleta tem {} anos\033[m" .format(anos))

if (anos <= 9):

    print("\033[1;30m Categoria MIRIM.\033[m")

elif (anos > 9 and anos <=14):

    print("\033[1;31m Categoria INFANTIL.\033[m")

elif (anos > 14 and anos <= 19):

    print("\033[1;32m Categoria JUNIOR.\033[m")

elif (anos > 19 and anos <= 25 ):

    print("\033[1;33m Categoria SêNIOR.\033[m")

elif (anos > 25):

    print("\033[7;34mCategoria MASTER.\033[m")