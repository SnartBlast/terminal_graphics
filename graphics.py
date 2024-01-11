import sys
import math
import os
import time

class Graphics():
    def __init__(self, window_modifier=1):
        # initialize class
        self.empty_space = '  '
        self.width = 49 * window_modifier
        self.height = 55
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        self.board = [[self.empty_space] * self.width for i in range(self.height)]    
        self.buffer = [[self.empty_space] * self.width for i in range(self.height)]    
        self.angle = 0.0


    def clear_board(self):
        # clear the board
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j] = self.empty_space
   

    def draw_line(self, x1, y1, x2, y2, option):
        # all given coordinates much be Integer value types
        x1 = round(x1)
        x2 = round(x2)
        y1 = round(y1)
        y2 = round(y2)
        self.draw_point_pixel(x1, y1)
        self.draw_point_pixel(x2, y2)
        
        # find slope and angle for line
        m = 0
        positive = True
        if (x2 - x1 != 0):
            m = (y2 - y1) / (x2 - x1) 
        degree = math.degrees(math.atan2(y2 - y1, x2 - x1))
        if (degree < 0):
            degree += 360
        self.angle = degree
        b = y1 - (x1 * m)
        absX = abs(x2 - x1)
        absY = abs(y2 - y1)
        startX = x1
        startY = y1
        if (x2 < x1):
            startX = x2
        if (y2 < y1):
            startY = y2
       
        # draw completely vertical line
        if (x1 == x2):
            for i in range(y1, y2):
                self.draw_point_pixel(x1, i)
            for i in range(y2, y1):
                self.draw_point_pixel(x1, i)
            return

        # if run is larger than rise
        elif (absY < absX):
            for i in range(round(startX), round(absX + startX)):
                y = m * i + b
                self.draw_point_pixel(i, y)

        # if rise if larger than run
        else:
            for i in range(round(startY), round(absY + startY)):
                x = (i / m) - (b / m)
                self.draw_point_pixel(x, i)


    def draw_point_pixel(self, x, y):
        # draw point as pixel
        ESC = '\x1b'
        if (self.board[round(y)][round(x)] == '::'):
            self.board[round(y)][round(x)] = '..'
        else:
            self.board[round(y)][round(x)] = '::'

   
    def print_board(self):
        # define ansi escape codes
        ESC = '\x1b'
        ODD = '[48;5;234m'
        EVEN = '[48;5;235m'
        TEXT = '[38;5;46m'
        SINGLE = '[48;5;53m'
        OVERLAP = '[48;5;54m'

        # print board with coordinates
        screen = ESC + TEXT + '    '
        for i in range(self.width):
            screen += str(i)
            if (i < 10):
                screen += ' '  

        # draw X coordinates
        screen += '\n    '
        for i in range(self.width):
            screen += '--'

        # draw Y coordinates
        for i in range(self.height):
            screen += '\n' 
            screen += str(i)
            if (i < 10):
                screen += ' '  
            screen += ' |'

            for j in range(self.width):
                if (self.board[i][j] == '  '):
                    if (j % 2 == 0):
                        screen += ESC + ODD + self.board[i][j]
                    else:
                        screen += ESC + EVEN + self.board[i][j]
                            
                elif (self.board[i][j] == '::'):
                    screen += ESC + SINGLE + '  '
                    screen += ESC + TEXT + ''
                else:
                    screen += ESC + OVERLAP + '  '
                    screen += ESC + TEXT + ''

        print(screen)
