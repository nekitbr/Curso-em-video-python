# criar um sorteador de 6 valores quantas vezes o usuario quiser
from random import randint
from time import sleep
lista=[]
while True:
    num=int(input('Quantos números quer sortear? '))
    num2=int(input('Quantos jogos sorteará? '))
    for vezes in range(0, num2):
        for sorteador in range(0, num):
            lista.append(randint(1,10))
        print(lista)
        sleep(0.3)
        lista.clear()
    a=input('Deseja sortear mais números?[S/N]').strip().upper()
    while a not in 'SN':
        print('Não entendi, use apenas as letras "S" ou "N"')
        a=input('Deseja sortear mais números?[S/N] ').strip().upper()
    if a in 'N':
        break