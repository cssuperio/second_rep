import pygame, sys

pygame.init()
black = (0,0,0)
white = (255,255,255)
size = [700, 500]
screen = pygame.display.set_mode(size)
img = pygame.image.load("Capture.PNG")
img = pygame.transform.scale(img, (150, 150))
pygame.display.set_caption("Bouncing Image")
clock = pygame.time.Clock()
x = 50
y = 50
changex = 5
changey = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            pygame.quit()
            sys.exit()
    x += changex
    y += changey

    if x > 550 or x < 0:
        changex =  changex * - 1
    if y > 350 or y < 0:
        changey = changey * -1
    screen.fill(black)
    screen.blit(img, (x, y))
    clock.tick(60)
    pygame.display.update()
