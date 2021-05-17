from random import randint
from time import sleep
print("-_"*12)
print("PEDRA PAPEL TESOURA")
print("-_"*12)
a=int(input("FAÇA SUA ESCOLHA!\n1 PARA PEDRA!\n2 PARA PAPEL!\n3 PARA TESOURA! "))
while a<=0 or a>=4:
    print("Você digitou algo incorretamente, por favor, selecione sua jogada!\n1 PARA PEDRA!\n2 PARA PAPEL!\n3 PARA TESOURA!")
    a=int(input())
b=randint(1,3)
print("#"*25)
print("ESCOLHENDO A JOGADA...")
print("#"*25)
sleep(1.5)
if a==3 and b==2:
    print("VOCÊ GANHOU! EU ESCOLHI PAPEL!")
elif a==1 and b==3:
    print("VOCÊ GANHOU! EU ESCOLHE TESOURA")
elif a==2 and b==1:
    print("VOCÊ GANHOU! EU ESCOLHI PEDRA!")
elif a==2 and b==3:
    print("VOCÊ PERDEU! EU ESCOLHI TESOURA!")
elif a==3 and b==1:
    print("VOCÊ PERDEU! EU ESCOLHI PEDRA!")
elif a==1 and b==2:
    print("VOCÊ PERDEU! EU ESCOLHI PAPEL!")
else:
    print("EMPATAMOS!")