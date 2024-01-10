import sys
import math

class Graphics():
    def __init__(self, width=49, height=53):
        # initialize class
        self.empty_space = '  '
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        self.board = [[self.empty_space] * width for i in range(height)]    
        self.angle = 0.0


    def clear_board(self):
        # clear the board
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j] = self.empty_space
   

    def draw_line(self, x1, y1, x2, y2, option):
        # all given coordinates much be Integer value types
        # find slope and angle for line
        m = 0
        positive = True
        if (x2 - x1 != 0):
            m = (y2 - y1) / (x2 - x1) 
        degree = round(math.degrees(math.atan2(y2 - y1, x2 - x1)))
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
                if (option == 0):
                    self.board[i][x1] = '| '
                else:
                    self.draw_point_pixel(i, x1)
            return

        # if run is larger than rise
        if (absY < absX):
            for i in range(round(startX), round(absX + startX)):
                y = m * i + b
                if (option == 0):
                    self.draw_point_line(i, y, degree)
                else:
                    self.draw_point_pixel(i, y)

        # if rise if larger than run
        else:
            for i in range(round(startY), round(absY + startY)):
                x = (i / m) - (b / m)
                if (option == 0):
                    self.draw_point_line(x, i, degree)
                else:
                    self.draw_point_pixel(x, i)
        

    def draw_point_line(self, x, y, degree):
        # draw point as line character
        if (self.board[int(y)][int(x)] == '[]'):
            self.board[int(y)][int(x)] = '::'
            return
        if (self.board[int(y)][int(x)] != '  '):
            self.board[int(y)][int(x)] = '[]'
            return

         
        if (315 <= abs(degree) <= 360 or 0 <= degree < 45):
            self.draw_horizontal(x, y)

        elif (45 <= abs(degree) < 80 or 225 < degree < 260):
            self.draw_diagonal0(x, y)

        elif (100 <= degree < 65 ):

            self.draw_diagonal1(x, y)
        else:
            self.draw_vertical(x, y)


    def draw_point_pixel(self, x, y):
        # draw point as pixel
        ESC = '\x1b'
        if (self.board[round(y)][round(x)] == '::'):
            self.board[round(y)][round(x)] = '..'
        else:
            self.board[round(y)][round(x)] = '::'



    def draw_horizontal(self, x, y):
        # draw horizontal line
        string = ''
        if (y % 1 < 0.33):
            string = '""'
        elif (0.33 < y % 1 < 0.66):
            string = '--'
        else:
            string = '__'
        self.board[int(y)][int(x)] = string


    def draw_diagonal0(self, x, y):
        # draw diagonal line
        string = ''
        if (x % 1 < 0.5):
            string = '\\'
        else:
            string = ' \\'
        self.board[int(y)][int(x)] = string


    def draw_diagonal1(self, x, y):
        # draw diagonal line
        string = ''
        if (x % 1 < 0.5):
            string = '/'
        else:
            string = ' /'
        self.board[int(y)][int(x)] = string


    def draw_vertical(self, x, y):
        # draw vertical lines
        string = ''
        if (x % 1 < 0.5):
            string = '| '
        else:
            string = ' |'
        self.board[int(y)][int(x)] = string

   
    def print_board(self):
        # define ansi escape codes
        ESC = '\x1b'
        ODD = '[48;5;234m'
        EVEN = '[48;5;235m'

        TEXT = '[38;5;46m'
        SINGLE = '[38;5;51m'
        OVERLAP = '[38;5;20m'

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
                    screen += ESC + SINGLE + self.board[i][j]
                    screen += ESC + TEXT + ''
                else:
                    screen += ESC + OVERLAP + self.board[i][j]
                    screen += ESC + TEXT + ''

#                screen += self.board[i][j]

        print(screen)
