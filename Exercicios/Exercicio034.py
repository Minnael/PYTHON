s = float(input("Qual é o salário do funcionário?"))
sb = (s * 15) / (100) + (s)
sa = (s * 10) / (100) + (s)

if (s <= 1250):
    print("Quem ganhava R${} passa a ganhar R${:.2f} agora." .format(s, sb))
else:
    print("Quem ganhava R${} passa a ganhar R${:.2f} agora." .format(s, sa))