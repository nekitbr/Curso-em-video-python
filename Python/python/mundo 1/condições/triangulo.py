a=float(input("Digite o comprimento do primeiro lado do triangulo: "))
b=float(input("Digite o comprimento do segundo lado do triangulo: "))
c=float(input("Digite o comprimento do terceiro lado do triangulo: "))
if a<b+c and b<c+a and c<a+b:
    print("Pode formar um triangulo!")
else:
    print("Não pode formar um triangulo!")