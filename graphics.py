import sys
import math
import os
import time

class Graphics():
    def __init__(self, window_modifier=1):
        # initialize class
        self.width = round(49 * window_modifier)
        self.height = round(55 * window_modifier)
        self.board = [['  '] * self.width for i in range(self.height)]    
        self.color = [['  '] * self.width for i in range(self.height)]    
        self.buffer = []
        sys.setrecursionlimit(10**6)


    def add_line(self, toople):
        # add tuple to buffer
        self.buffer.append(toople)
        self.buffer = sorted(self.buffer, reverse=True)


    def add_side(self, side, color):
        # add a series of line tuples to the buffer
        # from point 0, draw a series of lines between point 1 and point 2
        self.add_line((0, side[0], side[1], side[2], side[3], color))       
        self.add_line((0, side[2], side[3], side[4], side[5], color))       
        self.add_line((0, side[0], side[1], side[4], side[5], color))       

        center_x = round((side[0] + side[2] + side[4]) / 3) + 1
        center_y = round((side[1] + side[3] + side[4]) / 3) + 1

        print(center_x)
        print(center_y)
    
        self.draw_point_pixel(center_x, center_y, color)
        self.fill_side(center_y, center_x, color, 0)
    

    def fill_side(self, y, x, color, count):
        # recursively fill within the lines
        if (count > 5):
            return
        if (x < 0 or x > self.width + 1):
            return 
        if (y < 0 or y > self.height + 1):
            return 
        self.draw_point_pixel(x, y, color)
        
        if (self.color[y - 1][x] != color):
            self.fill_side(y - 1, x, color, count+1)
        if (self.color[y + 1][x] != color):
            self.fill_side(y + 1, x, color, count+1)
        if (self.color[y][x - 1] != color):
            self.fill_side(y, x - 1, color, count+1)
        if (self.color[y][x + 1] != color):
            self.fill_side(y, x + 1, color, count+1)



    def clear_board(self):
        # clear the board
        self.buffer = []
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j] = '  '
   

    def draw_line(self, x1, y1, x2, y2, color):
        # all given coordinates much be Integer value types
        x1 = round(x1)
        x2 = round(x2)
        y1 = round(y1)
        y2 = round(y2)
        self.draw_point_pixel(x1, y1, color)
        self.draw_point_pixel(x2, y2, color)
        
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
                self.draw_point_pixel(x1, i, color)
            for i in range(y2, y1):
                self.draw_point_pixel(x1, i, color)
            return

        # if run is larger than rise
        elif (absY < absX):
            for i in range(round(startX), round(absX + startX)):
                y = m * i + b
                self.draw_point_pixel(i, y, color)

        # if rise if larger than run
        else:
            for i in range(round(startY), round(absY + startY)):
                x = (i / m) - (b / m)
                self.draw_point_pixel(x, i, color)


    def draw_point_pixel(self, x, y, color):
        # draw point as pixel
        self.board[round(y)][round(x)] = '::'
        self.color[round(y)][round(x)] = color

   
    def print_board(self, option=0):
        # render all lines from buffer
        for i in range(len(self.buffer)):
            self.draw_line(self.buffer[i][1], self.buffer[i][2], 
                           self.buffer[i][3], self.buffer[i][4],
                           self.buffer[i][5])
        
        # define ansi escape codes
        ESC = '\x1b'
        ODD = '[48;5;234m'
        EVEN = '[48;5;235m'
        TEXT = '[38;5;46m'
        BORDER = '[48;5;46m'

        # print board with coordinates
        screen = ESC + TEXT + '    '
        for i in range(self.width):
            screen += str(i)
            if (i < 10):
                screen += ' '  

        # draw X coordinates
        screen += '\n  '
        for i in range(self.width + 1):
            screen += ESC + TEXT + '=='

        # draw Y coordinates
        for i in range(self.height):
            screen += '\n'
            screen += str(i)
            if (i < 10):
                screen += ' '  
            screen += ESC + TEXT + '||'


            for j in range(self.width):
                if (self.board[i][j] == '  '):
                    if (j % 2 == 0):
                        screen += ESC + ODD + self.board[i][j]
                    else:
                        screen += ESC + EVEN + self.board[i][j]
        
                elif (self.board[i][j] == '::'):
                    screen += ESC + '[38;5;3m' + ''
                    screen += ESC + self.color[i][j] + '††'
                    screen += ESC + TEXT + ''
                else:
                    screen += ESC + OVERLAP + '  '
                    screen += ESC + TEXT + ''

        screen += ESC + '\n'

        print(screen)
        if (option == 0):
            self.clear_board()
