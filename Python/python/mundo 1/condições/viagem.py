a=float(input("qual a distancia da viagem?"))
if a <= 200:
    print("sua passagem custará R${:.2f}".format(0.5*a))
else:
    print("sua passagem custará R${:.2f}".format(0.5*200+0.45*(a-200)))