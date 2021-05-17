while True:
    a=float(input("De qual número deseja ver a tabuada? [digite 0 para parar] "))
    if a == 0: break
    for tab in range (0,10):
        print(f"{a} X {tab} = {a*tab:>2}")
print("Programa encerrado!")