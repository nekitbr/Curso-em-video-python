a=int(input("Digite um número: "))
b=0
for aa in range(1, a+1):
    if a%aa==0:
        b+=1
if b==2:
    print("primo")
else: print("não primo")