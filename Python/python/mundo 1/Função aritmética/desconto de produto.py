prc=float(input("Para saber qual o novo valor do produto com desconto, digite o preço original deste produto "))
dscint=float(input("Agora digite seu desconto "))
dscnum=((dscint)/100)
print("O preço deste produto passou de R${:.2f} para R${:.2f}".format(prc, ((prc)-(prc)*(dscnum))))