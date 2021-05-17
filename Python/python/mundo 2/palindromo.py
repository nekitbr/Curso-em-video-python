a=input("Digite sua frase: ")
if a.replace(' ','')[::-1] == a.replace(' ',''):
    print("É palíndromo!")
else: print("Não é palíndromo")