import pygame , sys
from pygame .locals import *
pygame.init()
venta = pygame.display.set_mode((400,300))
pygame.display.set_caption('tutorial 6 metodo load y blit ')
Mi_imagen = pygame.image.load('imágenes/nave.png')
posX,posY =130,70
"""
posX = 130
posY = 70
"""
venta.blit(Mi_imagen,(posX,posY))
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()