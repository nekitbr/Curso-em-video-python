import pygame
# importa o pygame, não é recomendado importar apenas as funções a serem utilizadas, como o mixer

pygame.mixer.init() # inicializa o mixer do pygame
pygame.mixer.music.load('ajr_burn_the_house_down.mp3') # dá load na musica
pygame.mixer.music.play() # toca o que estiver carregado no mixer

input("Aperte enter para parar a musica ")

''' while(pygame.mixer.music.get_busy()): pass '''
# enquanto o mixer.music tá ocupado ele pausa o código na linha onde se encontra, mas prefiro utilizar
# o código da linha 8

''' print("A música terminou e o código retornou ao normal") '''
#uso a linha 14 apenas quando uso a linha 10

'''import os
print(os.getcwd()) ''' # SERVE PRA PEGAR O DIRETÓRIO NO QUAL O VS CODE TÁ USANDO
# Detectar o caminho do script e usá-lo como pasta raíz para carregar arquivos
# " (os.path.join(os.path.dirname(__file__), 'ajr_burn_the_house_down.mp3') "