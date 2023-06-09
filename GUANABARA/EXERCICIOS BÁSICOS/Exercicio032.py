from datetime import date

ab = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual:"))

if ab == 0:
    ab = date.today().year

if (ab % 4) == 0 and (ab % 100) !=0 or (ab % 400) == 0:
    print("O ano de {} é BISSEXTO" .format(ab))

else:
    print("O ano de {} não é BISSEXTO " .format(ab))