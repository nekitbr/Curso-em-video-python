a=float(input("Digite o valor de A: "))
b=float(input("Digite o valor de B: "))
c=float(input("Digite o valor de C: "))
delta=((b**2)-(4*a*c))
if delta==0:
    print("O valor de delta será 0, então ambos os resultados de X serão identicos, sendo ambos {}".format((-b/2*a)))
if delta<0:
    print("O valor de delta é menor que 0, resultando num número 'impossível', o cálculo é nulo.")
if delta>0:
    print("O valor de delta é {:.3f}, tendo como X' {:.3f} e X'' {:.3f}".format(delta, -b+delta**1/2, -b-delta**1/2))