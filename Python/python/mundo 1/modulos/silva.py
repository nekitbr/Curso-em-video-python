a=input("digite seu nome completo: ")
if a.upper().find('SILVA') >= 0:
    print('Seu nome contém "Silva".')

if a.upper().find('SILVA') == -1:
    print('Seu nome não contém "Silva".')