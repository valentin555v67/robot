import pygame , sys
from pygame .locals import *
from random import randint 
pygame.init()
venta = pygame.display.set_mode((400,300))
pygame.display.set_caption('tutorial 7 metodo random ')
Mi_imagen = pygame.image.load("Imágenes/nave.png")
posX=randint(10,300)
posY=randint(10,200)

print (posX,posY)
venta.blit(Mi_imagen,(posX,posY))
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()