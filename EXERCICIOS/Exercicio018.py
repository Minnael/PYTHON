import math
an = float(input("Digite o ângulo que você deseja:"))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print("O ângulo de {} possuí um seno de {:.2f}".format(an, sen))
print("O ângulo de {} possuí um cosseno de {:.2f}".format(an, cos))
print("O ângulo de {} possuí uma tangente de {:.2f}".format(an,tan))