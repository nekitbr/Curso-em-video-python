import datetime
a=datetime.date.today().year
b=int(input("Digite seu ano de nascimento: "))
c=a-b
if c == 18:
    print("Você deverá se alistar neste ano!")
elif c > 18:
    print("Você está atrasado em {} anos para o seu alistamento!".format(c-18))
else:
    print("Você deverá se alistar em {} anos!".format(18-c))