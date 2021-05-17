a=float(input("digite o numero que você quer dividir "))
b=float(input("digite o divisor "))
while b == 0:
    print("Impossível dividir por 0, a conta dára um número impossível")
    b=float(input("digite outro divisor que não seja 0 "))

print("O resultado da divisão é {}!".format(a/b))