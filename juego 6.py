import pygame , sys
from pygame .locals import *
from random import randint
pygame.init()
venta = pygame.display.set_mode((600,300))
pygame.display.set_caption('tutorial 8  Animaciones Básicas ')
Mi_imagen=pygame.image.load ('Imágenes/cohete pixel.png')
posX=200
posY=100

velocidad=5
blanco=(255,255,255)
derecha=True
while True:
    venta.fill(blanco)
    venta.blit(Mi_imagen,(posX,posY))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    if derecha==True:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        if posX<400:
            posX+=velocidad
        else:
            derecha=False
    else:
        if posX>1:
            posX-=velocidad       
        else:
            derecha=True    
    pygame.display.update() 
