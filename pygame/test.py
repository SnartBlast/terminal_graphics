#!/usr/bin/python

import pygame
from pygame.locals import *
import sys
import math
import time


if __name__ == '__main__':
    # Initialise screen
    width = 1000
    height = 700
    #increment = width * 0.5
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Basic Pygame program')

    
    RED = (255,0,0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    COLORS = [(250, 250, 250), RED, GREEN, BLUE]
    color_index = 1

    CURSOR = (200, 200, 150)
    CLEAR = (250, 250, 250)
    SCAN = (200, 200, 200)
    
    # board
    board = [[-1] * width for i in range(height)]


    clock = pygame.time.Clock()
    clock.tick(15)

    x = 10
    y = 10
    counter = 10
#    pygame.draw.rect(screen, CLEAR, pygame.Rect(0, 0, width, height))

    # Event loop
    while True:
        before = time.time()

        counter += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(1)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 8

        if keys[pygame.K_RIGHT]:
            x += 8

        if keys[pygame.K_UP]:  
            y -= 8

        if keys[pygame.K_DOWN]:
            y += 8

        if keys[pygame.K_SPACE]:
           board[x][y] = color_index
        
        if keys[pygame.K_RETURN]:
            if (counter > 7): 
                counter = 0
                if (color_index == 3):
                    color_index = 0
                else:
                    color_index += 1

        # clear screen
#        pygame.draw.rect(screen, CLEAR, pygame.Rect(0, 0, width, height))
        screen.fill(CLEAR)

        # draw the board
        for i in range(height):
            for j in range(width):
                #if (board[i][j] != -1):
                pygame.draw.rect(screen, COLORS[board[i][j]], pygame.Rect(i, j, 4, 4))


         # cursor
        pygame.draw.rect(screen, CURSOR, pygame.Rect(x-8, y, 8, 4))
        pygame.draw.rect(screen, CURSOR, pygame.Rect(x+4, y, 8, 4))
        pygame.draw.rect(screen, CURSOR, pygame.Rect(x, y-8, 4, 8))
        pygame.draw.rect(screen, CURSOR, pygame.Rect(x, y+4, 4, 8))
        pygame.draw.rect(screen, COLORS[color_index], pygame.Rect(x, y, 4, 4))
    
#        for i in range(1, height, 4):
#            pygame.draw.rect(screen, SCAN, pygame.Rect(0, i, width, 1))

        if (counter % 25 == 0):
            print(f'x  -> {x}, y  -> {y}\n')
        
#        after = time.time()
#        time.sleep(0.033 - (after - before))

        pygame.display.update()
        #pygame.display.flip()



