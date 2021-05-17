a=float(input("digite a primeira nota: "))
b=float(input("digite a segunda nota: "))
c=float(input("digite a terceira nota: "))
d=(a+b+c)/3
if d < 5:
    print("Sua média foi de {:.2f} e infelizmente você foi reprovado.".format(d))
elif d>= 7:
    print("Sua média foi de {:.2f} e você foi aprovado!".format(d))
else:
    print("Sua média foi de {:.2f} e você está de recuperação.".format(d))