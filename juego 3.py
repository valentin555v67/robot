import pygame , sys
from pygame .locals import *
pygame.init()
venta = pygame.display.set_mode((400,300))
pygame.display.set_caption('tutorial 5 dibuja figuras geometricas ')

pygame.draw.circle(venta,(8,70,120),(80,90),50)

pygame.draw.rect(venta,(130,70,70),(0,0,100,30))

pygame.draw.polygon(venta,(50,190,80),((140,0),(291,106),(237,277),(56,277),(0,106)))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()