a=float(input("digite seu salario atual: "))
if a <= 1250:
    print("seu salario passou de R${} para R${}".format(a,(0.15*a)+a))
else:
    print("seu salario passou de R${} para R${}".format(a,(0.10*a)+a))