print("==" * 14)
print("   10 TERMOS DE UMA PA")
print("==" * 14)

a1 = int(input("Primeiro termo:"))
r = int(input("Razão:"))
decimo = a1 + (10 - 1) * r

for c in range(a1,(decimo + r), r):

    print(c, end == " => ")

print("Acabou")