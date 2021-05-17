a=int(input("Quantos valores quer mostrar? "))
t1=0
t2=1
cont=2
t3=t1+t2
print('{} -> {} '.format(t1,t2),end='')
while cont<a:
    t3=t1+t2
    print('-> {} '.format(t3),end='')
    t1=t2
    t2=t3
    cont+=1