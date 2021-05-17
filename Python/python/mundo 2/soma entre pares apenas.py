s=0
aa=int(input("Quantos valores serão somados? "))
for b in range(1, aa+1):
    a=int(input("digite os valores:"))
    if a%2==0:
        s+=a
print(s)