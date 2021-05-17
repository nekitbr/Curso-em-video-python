a=(int(input('digite o primeiro: ')),int(input('digite o segundo: ')),int(input('digite o terceiro: ')),int(input('digite o quarto: ')))
print(f'você digitou {a}')
if a.count(9)>1: print(f'O valor 9 apareceu {a.count(9)} vezes')
elif a.count(9)==1: print(f'O valor 9 apareceu {a.count(9)} vez')
else: print('O valor 9 não apareceu')
if a.count(3)>0: print(f'O valor 3 apareceu na {a.index(3)+1}ª posição.')
else: print('O valor 3 não apareceu')
print(f'Os valores pares foram: ',end='')
for pares2 in a:
    if pares2%2==0:
        print(f'{pares2} ',end='')