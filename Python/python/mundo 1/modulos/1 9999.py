a = int(input("digite um número de 0 a 9999: "))
u = a // 1 % 10 
d = a // 10 % 10 #faz a divisão inteira por 10, ignorando o resto da divisão (9999/10=999) (9999/100=99)
c = a // 100 % 10 #o simbolo de porcentagem divide por 10 e usa apenas o resto da divisão
m = a // 1000 % 10 

print (a)
print("unidade", u)
print("dezena", d)
print("centena", c)
print("milhar", m)