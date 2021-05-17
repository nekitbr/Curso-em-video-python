lista=[]
while True:
    for inputs in range(1, int(input('Quantos valores serão adicionados? (Valores repetidos não serão adicionados) '))+1):
        num=float(input('Digite o que quer adicionar: '))
        if num not in lista:
            lista.append(num)
    a=str(input('Deseja adicionar mais valores? [S/N] ')).strip().upper()
    if a in 'N':
        print('Programa encerrado, obrigado!')
        break
    while a not in 'SN':
        a=str(input('Não entendi, Deseja adicionar mais valores? [S/N] ')).strip().upper()
lista.sort()
print('Você adicionou',len(lista),'valores na lista, sendo eles: ', end='')
for prints in lista:
    if prints!=max(lista):
        print(f'{prints}, ',end='')
    else: print(f'e {prints} ',end='')
print(f'. O menor da lista foi {min(lista)} na posição {lista.index(min(lista))+1} e {max(lista)} sendo o maior na posição {lista.index(max(lista))+1}')
print('A ordem crescente desses valores é',lista)
print('A ordem decresente desses valores é',list(reversed(lista)))
#dá pra usar lista[::-1] mas usar o list(reversed(lista)) é mais rapido, usa menos memória e melhor pra ler