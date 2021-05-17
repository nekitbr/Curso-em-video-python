a=float(input("qual o valor do empréstimo? "))
b=float(input("qual seu salário? "))
c=int(input("em quantos anos você deseja pagar? "))
d=a/(c*12)
if d>0.3*b:
    print("infelizmente nao podemos lhe conceder este impréstimo devido sua baixa renda comparado ao valor solicitado! ")
else:
    print("emprestimo aceito! O valor será de R${:.2f} mensais!".format(d))