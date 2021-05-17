c=0
e=1000
for a in range(1,6):
    b=float(input("digite o peso das pessoas: "))
    if b>c: c=b
    elif b<e: e=b
print("O menor peso foi",e,"e o maior foi",c)