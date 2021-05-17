a=('zero','um','dois','tres','quatro')
b=int(input('Digite um número de 0 a 4: '))
while b<0 or b>4:
    print('não entendi')
    b=int(input('Digite um número de 0 a 4: '))
print(a[b])