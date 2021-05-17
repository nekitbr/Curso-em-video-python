import math
oposto = float(input("Digite o comprimento do cateto oposto: "))
adj = float(input("Digite o comprimento do cateto adjacente: "))
print("O valor da hipotenusa será {:.3f}".format(math.hypot(oposto, adj)))
