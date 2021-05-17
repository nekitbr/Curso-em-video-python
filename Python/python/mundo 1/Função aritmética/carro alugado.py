d=int(input("Contando desde o dia do aluguel até a data de hoje, por quantos dias o carro foi alugado? "))
km=float(input("Quantos km o carro percorreu? "))
print("O preço total a ser pago é de R${:.f2}".format((d*60)+(km*0.15)))

## considero 60 reais por dia e 0.15 reais por km rodado