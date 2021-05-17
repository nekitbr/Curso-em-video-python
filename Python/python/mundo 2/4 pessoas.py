e = 0
f = ''
g = 0
# h=0
j = 0
for a in range(1, 5):
    b = input("Digite o nome da pessoa: ").strip()
    c = int(input("Digite a idade da pessoa: "))
    d = input("Digite o sexo da pessoa (F ou M): ").strip()
    if 'F' in d.upper() and c < 20:
        g += 1
    # elif d.upper().find('M')==0: h+=1
    if c > e:
        e = c
        f = b
    j += c
j = j/4
print('''A média de idades foi {:.2f} .
A pessoa mais velha é {}.
{} mulheres tem menos de 20 anos.'''.format(j, f, g))
