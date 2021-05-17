# ler nome e peso das pessoas, guardando tudo numa lista, mostrar quantas pessoas foram cadastradas, uma lista
# com as pessoas mais pesadas e outra com as mais leves
lista1=[]
lista2=[]
lista3=[]
for cadastrar in range(1,int(input('quantas pessoas serão cadastradas? '))+1):
    lista1.append(input('Nome? '))
    lista1.append(int(input('Idade? ')))
    if lista1[1] > 45:
        lista2+=lista1
        #lista2.append(lista1[:])
    else:
        lista3+=lista1
        #lista3.append(lista1[:])
    lista1.clear()
del(lista1)
print(f'As pessoas mais leves são {lista3} e as mais pesadas são {lista2}')