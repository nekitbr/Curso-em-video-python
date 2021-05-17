sal=float(input("digite seu salario atual, sem presente aumento R$"))
aumint=float(input("Agora digite, em números inteiros, o valor do aumento em porcentagem de seu salário "))
aumnum=((aumint)/100)
print("Seu salário passará de R${:.2f} para R${:.2f}".format(sal, (sal)*(aumnum)+(sal)))