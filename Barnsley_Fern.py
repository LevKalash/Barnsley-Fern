import pygame
import random
import sys

from pygame.locals import *
# importing libraries

pygame.init()  # Standart pygame initialisation

WIDTH = 600
HEIGHT = 800  # setting window size
detalisation = 30000  # setting detalisation of image (number of dots)

win = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)  # Making window

BGCOLOR = (0, 0, 0)
FERNCOLOR = (0, 166, 17)  # setting colors


def convert_point(tup):
    tup = list(tup)
    tup[0] = (tup[0] + 2.5) * ((WIDTH - 20)/5)
    tup[1] = HEIGHT - tup[1] * ((HEIGHT - 20)/10) - 10
    return tuple(tup)


def f1(point):
    x = 0
    y = 0.16 * point[1]
    return x, y


def f2(point):
    x = 0.85 * point[0] + 0.04 * point[1]
    y = -0.04 * point[0] + 0.85 * point[1] + 1.6
    return x, y


def f3(point):
    x = 0.20 * point[0] - 0.26 * point[1]
    y = 0.23 * point[0] + 0.22 * point[1] + 1.6
    return x, y


def f4(point):
    x = -0.15 * point[0] + 0.28 * point[1]
    y = 0.26 * point[0] + 0.24 * point[1] + 0.44
    return x, y


def main():
    point = (0, 0)
    win.fill(BGCOLOR)
    for i in range(detalisation + 1):
        win.fill(FERNCOLOR, (convert_point(point), (1, 1)))
        rand = random.random()

        pygame.draw.rect(win, BGCOLOR, (0, 0, 300, 30))
        win.blit(pygame.font.Font(None, 20).render(f"{i}/{detalisation}", 0, (255, 255, 255)), (5, 5))

        if rand <= 0.01:
            point = f1(point)
        elif rand <= 0.86:
            point = f2(point)
        elif rand <= 0.93:
            point = f3(point)
        else:
            point = f4(point)
        """   
        if   rand <= 0.01: point = f1(point)
        elif rand >  0.01 and rand <= 0.86: point = f2(point)
        elif rand >  0.86 and rand <= 0.93: point = f3(point)
        elif rand >  0.95 and rand <= 1.00: point = f4(point)
        """

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