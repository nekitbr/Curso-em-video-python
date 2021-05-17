a=int(input("Qual o número que deseja converter? "))
b=int(input('''E para qual base?
[1] para HEXADECIMAL
[2] para OCTAL
[3] para BINÁRIO
'''))
while b<1 or b>3:
    print(b, '''é uma opção inválida
    [1] para HEXADECIMAL
    [2] para OCTAL
    [3] para BINÁRIO''') 
    b=int(input())
if a < 0:
    if b == 1:
      print(hex(a)[3:])
    elif b == 2:
       print(oct(a)[3:])
    else: print(bin(a)[3:])
else:
    if b == 1:
        print(hex(a)[2:])
    elif b == 2:
        print(oct(a)[2:])
    else: print(bin(a)[2:])