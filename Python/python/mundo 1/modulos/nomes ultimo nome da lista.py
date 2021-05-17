nome = str(input("digite seu nome: ")).strip() # remove os espaços desnecessários, do começo e do fim

splitstrip = nome.split() # transforma a string em uma lista, separa os valores por espaço

print("Seu nome todo em maiúsculo é {}".format(nome.upper()))
print("Seu nome todo em minúsculo é {}".format(nome.lower()))

print("Seu nome tem {} caracteres sem contar os espaços".format(len(nome.replace(' ', '')))) # tira espaços
#                                                                                            # da string

print("Seu primeiro nome tem {} letras".format(len(splitstrip[0])))    

print("Seu primeiro nome é", splitstrip[0]) # mostra o primeiro valor da lista

print("Seu último nome é", splitstrip[len(splitstrip)-1]) # mostra splitstrip no valor de len -1, ou seja,
# vai mostrar (quantas strings existem na lista splitstrip -1), -1 pois a lista começa do 0 e o len
# começa do 1. Por exemplo, numa lista com 7 valores, iria mostrar o valor de (7-1)=6

#o código é feito das linhas 1 3 5 6 8 11 13 15, totalizando 8 linhas, o resto é espaçamento e comentário