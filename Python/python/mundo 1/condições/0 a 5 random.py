import random
a=random.randint(0, 10)
b=int(input("Tente adivinhar em que numero pensei, de 1 a 10: "))
c=1
while b < 0 or b > 10:
    b=int(input("b não é um número válido, digite um número de 1 a 10: "))
while b != a:
    print("Infelizmente você errou")
    b=int(input("Digite novamente: "))
    c+=1
else:
    print("Parabéns, você acertou e teve que fazer {} palpites!".format(c))