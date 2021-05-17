from time import sleep
from math import factorial
a = 0
while a != 7:
    soma = valor = maior = 0
    mult = 1
    menor = 9999
    a = int(input('''O que deseja fazer?
    [1] somar/subtrair
    [2] multiplicar
    [3] dividir
    [4] maior e menor
    [5] fatorial
    [6] raíz
    [7] sair\n'''))
    while a < 1 or a > 7:  # anti-crash
        a = int(input('''{} não é uma opção, digite sua opção:
        [1] somar
        [2] multiplicar
        [3] subtrair
        [4] dividir
        [5] maior
        [6] menor
        [7] sair\n'''.format(a)))
    if a == 1:  # somar ou subtrair
        b = int(input("Digite quantos valores serão somados: "))
        for eqsoma in range(1, b+1):
            soma += float(input("Digite o {}º valor: ".format(eqsoma)))
        print("A soma dos {} números foi {}".format(b, soma))
        sleep(0.6)

        sair = (input("Deseja sair do programa? [S/N] ")).strip().upper()
        while sair not in 'SN':
            sair = input("Opção inválida, por favor digite novamente, Deseja sair do programa? [S/N] ")
        if sair in 'S':
            a = 7
    elif a == 2:  # multiplicar
        b = int(input("Digite quantos valores serão multiplicados: "))
        for eqmult in range(1, b+1):
            mult *= float(input("Digite o {}º valor: ".format(eqmult)))
        print("A multiplicação dos {} valores foi {}".format(b, mult))
        sleep(0.6)

        sair = (input("Deseja sair do programa? [S/N] ")).strip().upper()
        while sair not in 'SN':
            sair = input("Opção inválida, por favor digite novamente, Deseja sair do programa? [S/N] ")
        if sair in 'S':
            a = 7
    elif a == 3:  # dividir
        b = float(input("Digite o dividendo: "))
        c = float(input("Digite o divisor: "))
        while c == 0:
            c = float(input("0 não pode ser um divisor, digite outro valor: "))
        print("O resultado de {} ÷ {} foi {}".format(b, c, b/c))
        sleep(0.6)

        sair = (input("Deseja sair do programa? [S/N] ")).strip().upper()
        while sair not in 'SN':
            sair = input("Opção inválida, por favor digite novamente, Deseja sair do programa? [S/N] ")
        if sair in 'S':
            a = 7
    elif a == 4:  # maior e menor
        b = int(input("Digite quantos valores serão comparados: "))
        for eqmaior in range(1, b+1):
            valor = float(input("Digite o {}º valor: ".format(eqmaior)))
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
        print("Dos {} valores solicitados, o maior é {} e o menor é {}".format(
            eqmaior, maior, menor))
        sleep(0.6)

        sair = (input("Deseja sair do programa? [S/N] ")).strip().upper()
        while sair not in 'SN':
            sair = input("Opção inválida, por favor digite novamente, Deseja sair do programa? [S/N] ")
        if sair in 'S':
            a = 7
    elif a == 5:  # fatorial
        b = float(input("Digite o numero a ser fatorado: "))
        print("A fatoração de {} é {}".format(b, factorial(b)))
        sleep(0.6)

        sair = (input("Deseja sair do programa? [S/N] ")).strip().upper()
        while sair not in 'SN':
            sair = input("Opção inválida, por favor digite novamente, Deseja sair do programa? [S/N] ")
        if sair in 'S':
            a = 7
    elif a == 6:  # raíz
        b = float(input("De que número você quer a raíz? "))
        c = int(input("E a qual potência será?"))
        print("O resultado de {}√{} é {}".format(c, b, b**(1/c)))
        sleep(1.6)

        sair = (input("Deseja sair do programa? [S/N] ")).strip().upper()
        while sair not in 'SN':
            sair = input("Opção inválida, por favor digite novamente, Deseja sair do programa? [S/N] ")
        if sair in 'S':
            a = 7
print("Programa encerrado, obrigado!")
