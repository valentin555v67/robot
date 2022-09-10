import pygame , sys
from pygame .locals import *
from random import randint
pygame.init()
venta = pygame.display.set_mode((600,300))
pygame.display.set_caption('tutorial 10 uso del cursor ')
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
        elif evento.type ==pygame.KEYDOWN: 
            if evento.key==K_LEFT:
               posX -=velocidad 
            elif evento.key==K_RIGHT:
                posX+=velocidad    
        elif evento.type ==pygame.KEYUP:
            if evento.key== K_LEFT:
               print(" tecla isquierda libre") 
            elif evento.key==K_RIGHT:
               print(" tecla derecha libre")   
    posX,posY= pygame.mouse.get_pos()     
    posX=posX-100
    posY=posY-50     
    pygame.display.update() 
