import pygame , sys
from pygame .locals import *
pygame.init()
venta = pygame.display.set_mode((400,300))
pygame.display.set_caption('tutorial 4 dibuja linea')
Color= pygame.Color(50,90,150)
pygame.draw.line(venta,Color,(60,80),(160,100),100)
print(Color.b)
Color= pygame.Color(60,50,160)
pygame.draw.line(venta,Color,(60,80),(160,100),40)
print(Color.r) 
Color= pygame.Color(80,70,120)
pygame.draw.line(venta,Color,(90,90),(130,80),30)
print(Color.g)
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
