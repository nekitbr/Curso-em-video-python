a=float(input("digite o valor a ser pago: "))
while a <= 0:
    a=float(input(a, "não é um valor válido, por favor digite novamente: "))
b=int(input("Como deseja pagar?\n0 para à vista no boleto\n1 para à vista no cartão\n2 para parcelas múltiplas no cartão\n"))
while b < 0 or b > 2:
    b=int(input(b, "não é uma opção por favor escolha novamente\n0 para à vista no boleto\n1 para à vista no cartão\n2 para parcelas múltiplas no cartão\n"))
if b == 0:
    print("O valor a ser pago será R${:.2f}".format(a*0.9))
elif b == 1:
    print("O valor a ser pago será R${:.2f}".format(a*0.95))
elif b == 2:
    p=int(input("Em quantas vezes irá pagar? "))
    while p <= 0:
        print(p, "não é um tempo (em meses) válido, para esta opção, deverá ser no mínimo 2 parcelas\n Digite em quantas parcelas você pagará: ")
        p=int(input())
    if p == 1:
        print("O valor a ser pago será R${:.2f} à vista no cartão".format(a*0.95))
    elif p == 2:
        print("O valor a ser pago será de R${:.2f} ao mês, totalizando R${:.2f}".format(a/p, a))
    else:
        print("O valor a ser pago será de R${:.2f} ao mês, totalizando R${:.2f}".format((a*1.3)/p, a*1.3))
        