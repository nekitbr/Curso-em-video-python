# uma lista dentro doutra lista com valores pares e outra com ímpares
# mostrar esses valores em ordem crescente
lista1=[[],[]]
for valores in range(0,int(input('Quantos valores? '))):
    a=int(input('Digite valores: '))
    if a%2==0:
        lista1[0].append(a)
    else: lista1[1].append(a)
print(f'Os valores pares são {lista1[0]} e os ímpares {lista1[1]}')