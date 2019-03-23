import math
o = float(input("Comprimento do cateto oposto:"))
a = float(input("Comprimento do cateto adjacente:"))
h = math.hypot(o, a)
print("A hipotenusa vai medir {:.2f}".format(h))