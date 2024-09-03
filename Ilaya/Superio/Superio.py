import pygame
pygame.init()
black = (0,0,0)
white = (255,255,255)
green =(0,255,0)
red = (255,0,0)
blue = (0, 0, 255)

def draw(screen, x, y):
    # pygame.draw.ellipse(screen, blue, [x, y, 10, 10])
    # pygame.draw.line(screen, red, [5+x, 17+y], [5+x, 7+y], 2)
    # pygame.draw.line(screen, red, [5+x, 7+y], [10+x, 17+y], 2)
    # pygame.draw.line(screen, red, [5+x, 7+y], [x, 17+y], 2)
    # pygame.draw.line(screen, blue, [5+x, 17+y], [10+x, 27+y], 2)
    # pygame.draw.line(screen, blue, [5+x, 17+y], [x, 27+y], 2)
    pygame.draw.rect(screen, black, [x,y, 100, 100])

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Keyboard Event")
clock = pygame.time.Clock()
x = 10
y = 10
changex = 0
changey = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changex = -3
            elif event.key == pygame.K_RIGHT:
                changex = 3
            elif event.key == pygame.K_UP:
                changey = -3
            elif event.key == pygame.K_DOWN:
                changey = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changex = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                changey = 0
        if x > 600:
            x = 0
        if x < 0:
            x = 600
        if y > 400:
            y = 0
        if y < 0:
            y = 400
    x += changex
    y += changey
    screen.fill(white)
    draw(screen, x, y)
    pygame.display.update()
    clock.tick(60)
