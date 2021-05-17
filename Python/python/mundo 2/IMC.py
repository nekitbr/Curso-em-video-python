a=float(input("digite sua massa corpórea: "))
b=float(input("digite sua altura: "))
c=a/(b**2)
if c < 18.5:
    print("abaixo do peso")
elif c >= 18.5 and c < 25:
    print("peso ideal")
elif c >= 25 and c < 30:
    print("sobrepeso")
elif c >= 30 and c < 40:
    print("obesidade")
else: print("obesidade mórbida")