import pygame
import random
import sys

from pygame.locals import *
# importing libraries

pygame.init()  # Standart pygame initialisation

WIDTH = 600
HEIGHT = 800  # setting window size
detalisation = 50000  # setting detalisation of image (number of dots)

win = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)  # Making window

BGCOLOR = (0, 0, 0)
FERNCOLOR = (0, 166, 17)  # setting colors


cooficients = [
    {'x':[0, 0], 'y':[0, 0.16], 'e':0},
    {'x':[0.85, 0.04], 'y':[-0.04, 0.85], 'e':1.6},
    {'x':[0.20, -0.26], 'y':[0.23, 0.22], 'e':1.6},
    {'x':[-0.15, 0.28], 'y':[0.26, 0.24], 'e':0.44}
]


def NewDotCoordSetter(point, coofs):
    x = coofs['x'][0] * point[0] + coofs['x'][1] * point[1]
    y = coofs['y'][0] * point[0] + coofs['y'][1] * point[1] + coofs["e"]
    print(x, y)
    return x, y


def convert_point(tup):
    tup = list(tup)
    tup[0] = (tup[0] + 2.5) * ((WIDTH - 20)/5)
    tup[1] = HEIGHT - tup[1] * ((HEIGHT - 20)/10) - 10
    return tuple(tup)  # Понять что за коэффициенты добавляются вычитаются и почему делится именно на это


def main():
    point = (0, 0)
    win.fill(BGCOLOR)
    for i in range(detalisation + 1):
        win.fill(FERNCOLOR, (convert_point(point), (1, 1)))
        rand = random.random()

        pygame.draw.rect(win, BGCOLOR, (0, 0, 300, 30))
        win.blit(pygame.font.Font(None, 20).render(f'{i}/{detalisation}\n Press "q" to quit, True, (255, 255, 255)), (5, 5))

        if rand <= 0.01:
            point = NewDotCoordSetter(point, cooficients[0])
        elif rand <= 0.86:
            point = NewDotCoordSetter(point, cooficients[1])
        elif rand <= 0.93:
            point = NewDotCoordSetter(point, cooficients[2])
        else:
            point = NewDotCoordSetter(point, cooficients[3])

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                    sys.exit()

if __name__ == '__main__':
    main()