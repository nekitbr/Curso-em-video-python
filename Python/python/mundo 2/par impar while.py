from random import randint
cont=0
a=input("Par ou ímpar?\n").strip().upper()
while True:
    b=int(input("Qual número você escolhe?\n"))
    c=randint(1,10)
    if (b+c)%2 == 0 and a[0] in 'P':
        print(f"{b}+{c}={b+c} \nVocê venceu! programa encerrado.")
        break
    elif (b+c)%2 == 1 and a[0] not in 'P':
        print(f"{b}+{c}={b+c} \nVocê venceu! programa encerrado.")
        break
    else: 
        print(f"{b}+{c}={b+c} \nVocê perdeu! Vamos de novo!")
        cont+=1
print(f"Você teve um total de {cont+1} tentativas para me derrotar!")