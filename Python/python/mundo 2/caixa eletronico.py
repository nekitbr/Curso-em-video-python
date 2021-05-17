from time import sleep

while True:
    try:
        a=int(input('Qual o valor deseja sacar?\n'))
        print(f'''Serão:
        {a//50} notas de 50;
        {a%50//20} nota(s) de 20 reais;
        {a%50%20//10} nota(s) de 10 reais;
        {a%50%20%10//5} nota(s) de 5 reais;
        {a%50%20%10%5//1} nota(s) de 1 real.''')
        break
    except:
        print('Informação inválida, tente novamente.')
        sleep(0.7)