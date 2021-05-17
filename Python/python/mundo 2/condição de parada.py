somar=cont=0
while True:
    soma=float(input("Digite números a serem somados e digite 999 para parar: "))
    if soma==999: break
    somar+=soma
    cont+=1
print (f"O resultado dos {cont} números foi {somar}")