alt=float(input("Diga a altura da parede na qual deseja pintar"))
larg=float(input("Diga a largura da parede na qual deseja pintar"))
altlarg=(alt)*(larg)
print("esta parede é constituida de {}m² e você precisará de aproximadamente {}L de tinta".format(altlarg, (altlarg)/2))

## considero que a cada 2m² é consumido 1L de tinta