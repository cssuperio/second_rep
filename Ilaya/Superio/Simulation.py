

import pygame, random, sys
from pygame.locals import *


pygame.init()

colours = [(0,0,0), (255, 255, 255), (176, 210, 78)]


size = (1000, 700)
surface = pygame.display.set_mode(size)
pygame.display.set_caption("Moving Background")

clock = pygame.time.Clock()



xr = 485
xc = 500

xr2 = random.randint(0, 1000)
xc2 = int((xr2 + xr2 + 30)/2)

xr3 = random.randrange(0, 1000)
xc3 = int((xr3 + xr3 + 30)/2)
dx = 10
dx2 = int(random.randint(7, 14))
dx3 = int(random.randint(7, 12))

def sprite(surface, colour, xr, xc, xr2, xc2, xr3, xc3):

    

    pygame.draw.rect(surface, colours[1], (0, 480, 1000, 30))

    pygame.draw.rect(surface, colours[2], (xr, 190, 30, 290))
    pygame.draw.circle(surface, colours[1], (xc, 140), 50)

    
    pygame.draw.rect(surface, colours[2], (xr2, 240, 30, 240))
    pygame.draw.circle(surface, colours[1], (xc2, 190), 50)


    pygame.draw.rect(surface, colours[2], (xr3, 300, 30, 180))
    pygame.draw.circle(surface, colours[1], (xc3, 250), 50)


while True:

    for event in pygame.event.get():

        if event.type == (QUIT):

            pygame.quit()
            sys.exit()


    if xc < 0:
        xc = 1000

    elif xc > 1000:
        xc = 0
        

    if xr < 0:
        xr = 1000

    elif xr > 1000:
        xr = 0

    if xc2 < 0:
        xc2 = 1000

    elif xc2 > 1000:
        xc2 = 0

    if xr2 < 0:
        xr2 = 1000

    elif xr2 > 1000:
        xr2 = 0

    if xc3 < 0:
        xc3 = 1000

    elif xc3 > 1000:
        xc3 = 0

    if xr3 < 0:
        xr3 = 1000

    elif xr3 > 1000:
        xr3 = 0
    
    xc += dx
    xr += dx

    xc2 += dx2
    xr2 += dx2

    xc3 += dx3
    xr3 += dx3

    surface.fill(colours[0])
    sprite(surface, colours, xr, xc,  xr2, xc2, xr3, xc3)

    pygame.display.update()
    clock.tick(56)

    
