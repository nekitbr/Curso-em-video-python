a = int(input("Digite o inicio da PA: "))
b = int(input("Digite o fim da PA: "))
c = int(input("Digite a razão da PA: "))
if a < b and c > 0:
    for d in range(a, b+1, c):
        print(d)
elif a > b and c > 0:
    for d in range(a, b-1, c*-1):
        print(d)
elif a < b and c < 0:
    for d in range(b, a-1, c):
        print(d)
else:
    for d in range(b, a+1, c*-1):
        print(d)
