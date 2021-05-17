# fazer uma matriz 3x3, depois mostrar a matriz com os números, a soma dos valores pares, ímpares, e da
# coluna em que o úsuario escolher
lista=[]
for l in range(1,4):
    for c in range(1,4):
        lista.append(int(input(f'Digite um valor inteiro para coluna {c} linha {l}: ')))
for print1 in range(0,3):
    print(f'[{lista[print1]:^5}] ',end='')
print('')
for print2 in range(3,6):
    print(f'[{lista[print2]:^5}] ',end='')
print('')
for print3 in range(6,9):
    print(f'[{lista[print3]:^5}] ',end='')

# print(f'''
# [{a}] [{b}] [{c}]
# [{d}] [{e}] [{f}]
# [{g}] [{h}] [{i}]''')