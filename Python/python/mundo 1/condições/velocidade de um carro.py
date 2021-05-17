a=int(input("Qual a velocidade do carro? "))
if a > 80:
    print("voce foi multado em R${:.2f}".format(7*(a-80)))
else:
    print('você está dentro dos limites da velocidade')