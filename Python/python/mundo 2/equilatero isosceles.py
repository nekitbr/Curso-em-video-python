while True:
    L1 = float(input("Digite o valor do primeiro lado: "))
    L2 = float(input("Digite o valor do segundo lado: "))
    L3 = float(input("Digite o valor do terceiro lado: "))
    if L1+L2 <= L3 or L1+L3 <= L2 or L2+L3 <= L1 or (L1 == L2 == L3 == 0):
        print("Com as medidas usadas acima, não é possível formar um triângulo,\nlogo, não será nem Equilatero, Escaleno ou Isósceles")
    else:
        if L1 == L2 == L3:
            print("O triângulo é Equilatero")
        elif L1 != L2 != L3 != L1:
            print("O triângulo é Escaleno")
        else:
            print("O Triângulo é Isósceles")
    parar = input('Deseja fazer outra verificação? [S/N]\n').strip().upper()
    while parar not in 'SsNn':
        parar = input(
            'Desculpe, não entendi\nDeseja fazer outra verificação?\nLembrando que só aceito respostas de 1 letra! [S/N]')
    if parar in 'Nn':
        break
