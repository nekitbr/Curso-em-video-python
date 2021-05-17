din=float(input("quanto dinheiro você possui em reais? R$"))
dol=float(input("quanto está o valor do dólar hoje? US$"))
print("com R${:.2f} você pode ter até ${:.2f}!".format (din, ((din)/(dol))))