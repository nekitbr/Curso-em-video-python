from datetime import date
a=int(input("digite um ano para ser analisado, digite 0 para analisar o ano atual: "))
if a == 0:
    a=date.today().year
if (a % 4 == 0 and a % 100) or (a % 400 == 0):
    print("bissexto!")
else:
    print("nao é bissexto!")


# Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
# Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)