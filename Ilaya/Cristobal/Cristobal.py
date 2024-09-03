import pygame
pygame.init()
black = (0,0,0)
white = (255,255,255)
green =(0,255,0)
red = (255,0,0)
blue = (0, 0, 255)

def draw(screen, x, y):
    pygame.draw.ellipse(screen, blue, [x, y, 10, 10])
    pygame.draw.line(screen, red, [5+x, 17+y], [5+x, 7+y], 2)
    pygame.draw.line(screen, red, [5+x, 7+y], [10+x, 17+y], 2)
    pygame.draw.line(screen, red, [5+x, 7+y], [x, 17+y], 2)
    pygame.draw.line(screen, blue, [5+x, 17+y], [10+x, 27+y], 2)
    pygame.draw.line(screen, blue, [5+x, 17+y], [x, 27+y], 2)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mouse Event")
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(green)
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill(white)
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    draw(screen, x, y)
    pygame.display.update()
    clock.tick(60)
