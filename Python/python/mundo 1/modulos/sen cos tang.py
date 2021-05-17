from math import sin, cos, tan, radians
ang=int(input("Digite um ângulo: "))
radang=radians(ang)
print("Seu seno é {:.3f}".format(sin(radang)))
print("Seu cosseno é {:.3f}".format(cos(radang)))
print("Sua tangente é {:.3f}".format(tan(radang)))