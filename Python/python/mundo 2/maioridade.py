from datetime import date
c=0
d=0
for a in range(1,8):
    b=int(input("Digite o ano de nascimento dessa pessoa: "))
    if date.today().year-b >= 21:
        c+=1
    elif date.today().year-b < 21: d+=1
print(c,'pessoas já atingiram a maioridade e',d,'ainda não')