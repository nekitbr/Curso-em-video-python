a=int(input("Digite a idade do atleta: "))
if a <= 9:
    print("MIRIM")
elif a>9 and a <= 14:
    print("INFANTIL")
elif a>14 and a <= 19:
    print("JUNIOR")
elif a> 19 and a <= 20:
    print("SENIOR")
else:
    print("MASTER")