import sys
import math

class Graphics():
    def __init__(self, width=49, height=54, background='235', accent='214'):
        # initialize class
        self.width = width
        self.height = height
        self.background_color = background
        self.accent_color = accent
        self.board = [[self.background_color] * self.width for i in range(self.height)]    
        self.buffer = []

        # remove default recursion limit
        sys.setrecursionlimit(10**6)


    def add_buffer_item(self, item):
        # add itemt to buffer
        self.buffer.append(item)
        self.buffer = sorted(self.buffer, reverse=True)       


    def draw_polygon(self, x1, y1, x2, y2, x3, y3, color):
        # fill in space between 3 points
        center_x = round((x1 + x2 + x3) / 3)
        center_y = round((y1 + y2 + y3) / 3)
        range_x = max([x1, x2, x3]) - min([x1, x2, x3])
        range_y = max([y1, y2, y3]) - min([y1, y2, y3])

        # round coordinate variables
        x1 = round(x1)
        x2 = round(x2)
        x3 = round(x3)
        y1 = round(y1)
        y2 = round(y2)
        y3 = round(y3)
        
        # draw border lines and fill
        self.draw_line(x1, y1, x2, y2, color)
        self.draw_line(x2, y2, x3, y3, color)
        self.draw_line(x1, y1, x3, y3, color) 

        if (not self.detect_inline(x1, y1, x2, y2, x3, y3)):
            self.fill(center_x, center_y, color)
        self.draw_line(x1, y1, center_x, center_y, color)
        self.draw_line(x2, y2, center_x, center_y, color)
        self.draw_line(x3, y3, center_x, center_y, color)
#        self.draw_pixel(center_x, center_y, 16)


    def detect_inline(self, x1, y1, x2, y2, x3, y3):
        # detect if all three points are in a line to prevent recursive overflow
        return (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2)

#        print('detect_inline HERE') 
        

    
    def fill(self, x, y, color):
        # recursively fill polygon
        if (self.board[y][x] == color):
            return 

        self.draw_pixel(x, y, color)
        if (x - 1 > 0):
            self.fill(x - 1, y, color)
        if (x + 1 < self.width):
            self.fill(x + 1, y, color)
        self.fill(x, y - 1, color)
        self.fill(x, y + 1, color)        


    def draw_line(self, x1, y1, x2, y2, color):
        # all given coordinates much be Integer value types
        x1 = round(x1)
        x2 = round(x2)
        y1 = round(y1)
        y2 = round(y2)
        self.draw_pixel(x1, y1, color)
        self.draw_pixel(x2, y2, color)
        
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
                self.draw_pixel(x1, i, color)
            for i in range(y2, y1):
                self.draw_pixel(x1, i, color)
            return

        # if run is larger than rise
        elif (absY < absX):
            for i in range(round(startX), round(absX + startX)):
                y = m * i + b
                self.draw_pixel(i, y, color)

        # if rise if larger than run
        else:
            for i in range(round(startY), round(absY + startY)):
                x = (i / m) - (b / m)
                self.draw_pixel(x, i, color)


    def draw_pixel(self, x, y, color):
        # draw point as pixel on board
        self.board[round(y)][round(x)] = str(color)


    def clear(self):
        # empty the buffer and board
        self.buffer = []
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j] = self.background_color


    def print(self, option=0):
        # render buffer items to board
        for i in range(len(self.buffer)):
            # add item to buffer
            # POLYGON FORMAT            LINE FORMAT 
            # item[0] = average z-axis       ''
            # item[1] = x1                   ''
            # item[2] = y1                   ''
            # item[3] = z1                   ''
            # item[4] = x2                   ''
            # item[5] = y2                   ''
            # item[6] = z2                   ''
            # item[7] = x3              item[7] = Ansi Escape Color Code
            # item[8] = y3                   
            # item[9] = z3                  
            # item[10] = Ansi Escape Color Code
            item = self.buffer[i]
            if (len(item) == 8):
                # draw line
                self.draw_line(item[1], item[2], item[4], item[5], item[7])                
            else:
                # draw polygon
                self.draw_polygon(item[1], item[2], item[4], item[5], item[7], item[8], item[10])

        # print the board    
        ESC = '\x1b'
        TEXT = '[38;5;247m'
        SHAPE = f'[38;5;{self.accent_color}m'
        NUMBER = '[48;5;237m'
        BORDER = '[48;5;130m' 
        screen = ESC + TEXT + ''
        screen += ESC + NUMBER + '     '
        for i in range(self.width - 1):
            screen += str(i)
            if (i < 10):
                screen += ' '
        screen += '  \n   '
        for i in range(self.width + 1):
            screen += ESC + BORDER + '  '
    
        for i in range(self.height):
            screen += ESC + NUMBER + f'\n{str(i)} '
            if (i < 10):
                screen += ' '
            screen += ESC + BORDER + '  '

            # DRAW SCREEN
            #-----------------------------------------------------------------
            for j in range(self.width - 1):
                if (self.board[i][j] != self.background_color):
                    # if we're rendering a shape
                    screen += ESC + SHAPE + ''
                    screen += ESC + '[48;5;' + self.board[i][j] + 'm††'
                    #screen += ESC + '[48;5;' + self.board[i][j] + 'm  '
                else:
                    # if we're rendering background
                    screen += ESC + TEXT + ''
                    screen += ESC + '[48;5;' + self.board[i][j] + 'm  '                
            #-----------------------------------------------------------------
                if (j == self.width - 2):
                    screen += ESC + BORDER + '  '
            if (i == self.height - 1):
                screen += ESC + NUMBER + '   '
                for k in range(self.width + 1):
                    screen += ESC + BORDER + '  '

        print(screen) 
