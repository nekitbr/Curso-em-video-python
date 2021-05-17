asplit=input("Digite o nome da cidade:  ").strip().split()
if asplit[0].upper() == 'SANTO':
    print("O primeiro nome da cidade é Santo.")
if asplit[0].upper() != 'SANTO':
    print("O primeiro nome da cidade não é Santo.")