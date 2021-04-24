import pygame, sys

from pygame.locals import  *

pygame.init()

size=(600,600)
screen=pygame.display.set_mode(size)
pygame.display.set_caption('ping_pong')

navy_blue = [0, 0, 128]
white = [255, 255, 255]
orange = [255, 165, 0]
black = [0, 0, 0]

y_movement1 = 267.5
y_movement2 = 267.5
x_velocity = 300
y_velocity = 300
gy = 25
sp2 = 585
sp1 = 15

def borders():
    pygame.draw.rect(screen, navy_blue, (0, 0, 600, gy) )
    pygame.draw.rect(screen, navy_blue, (0, 600, 600, -gy))

def objects():
    pygame.draw.rect(screen, orange, (sp1, y_movement1, 10, 25))
    pygame.draw.rect(screen, orange, (sp2, y_movement2, -10, 25))
    pygame.draw.rect(screen, white, (x_velocity, y_velocity, 7.5, 7.5))

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(15)

    event = pygame.event.get()

    borders()
    objects()

    x_velocity += 5
    y_velocity -= 5

    if y_velocity < gy:
        x_velocity += 5
        y_velocity += 5
    if x_velocity == 600:
        x_velocity = 300
        y_velocity = 300
    if x_velocity == 0:
        x_velocity = 300
        y_velocity = 300
    if x_velocity + 7.5 == sp2 and y_velocity < 300:
        x_velocity -= 5
        y_velocity += 5
    if x_velocity + 7.5 ==  sp2 and y_velocity > 300:
        x_velocity -= 5
        y_velocity -= 5
    if x_velocity == sp1 and y_velocity < 300:
        x_velocity += 5
        y_velocity += 5
    if x_velocity == sp1 and y_velocity > 300:
        x_velocity += 5
        y_velocity -= 5


    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and  y_movement1 > 25:
        y_movement1 -= 6
    if keys[pygame.K_s] and  y_movement1 < 575 - 25 -6 :
        y_movement1 += 6
    if keys[pygame.K_u] and y_movement2 > 25:
        y_movement2 -= 6
    if keys[pygame.K_j] and y_movement2 < 550 - 25 - 6:
        y_movement2 += 6

    screen.fill(black)

    borders()
    objects()

    for event in event:
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        else:
            pygame.display.flip( )

pygame.quit()
