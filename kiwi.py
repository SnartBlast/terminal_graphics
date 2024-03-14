import random
import math 

class Kiwi():
    # Kiwi's Noise Generator, based off of Perlin Noise
    def __init__(self, width, height):
        self.width = width
        self.height = height 
        self.buffer = [[0] * (self.width) for i in range(self.height)]
        self.vectors = [[0] * (self.width) for i in range(self.height)]

        # create base noise 
        self.make_vectors()
        self.smooth()
        self.sharpen(0.15)
        self.smooth()
    
    
    def make_vectors(self):
        # populate self.vectors with vectors
        # -----------------------------
        # | \ |   |   |_- |   |   |   |
        # -----------------------------
        # |   |  /|   |   |   |   |   |
        # -----------------------------
        # |   |   |   |   |   |   |   |
        # -----------------------------
        # |   |   |   |   |   |   |   |
        # -----------------------------
        # |   |   |   |   |   |   |   |
        # -----------------------------
        # |   |   |   |   |   |   |   |
        # -----------------------------
        # |   |   |   |   |   |   |   |
        # -----------------------------
        for i in range(1, len(self.vectors) - 1):  
            for j in range(1, len(self.vectors[0]) - 1):
                # get direction and magnitude of each vector
                direction = random.randint(0, 359)
                magnitude = random.randint(1, 100) / 100

                if (0 <= direction < 90):
                    self.vectors[i - 1][j + 1] += magnitude
                elif (90 <= direction < 180):
                    self.vectors[i - 1][j - 1] += magnitude
                elif (180 <= direction < 270):
                    self.vectors[i + 1][j - 1] += magnitude
                else:
                    self.vectors[i + 1][j + 1] += magnitude


    def smooth(self):
        # blend pixel values for smoothing effect
        for i in range(1, len(self.vectors) - 1):
            for j in range(1, len(self.vectors[0]) - 1):
                value = 0.0
                value += self.vectors[i-1][j-1]
                value += self.vectors[i-1][j]
                value += self.vectors[i-1][j+1]
                value += self.vectors[i][j-1]
                value += self.vectors[i][j]
                value += self.vectors[i][j+1]
                value += self.vectors[i+1][j-1]
                value += self.vectors[i+1][j]
                value += self.vectors[i+1][j+1]
                value = value / 9
                self.buffer[i][j] = value

        # copy buffer to vectors board
        for i in range(len(self.vectors)):
            for j in range(len(self.vectors[0])):
                self.vectors[i][j] = self.buffer[i][j]

        
        # restore edges
        for i in range(len(self.vectors)):
            self.vectors[i][0] = 0.5
            self.vectors[i][self.width - 1] = 0.3
        for i in range(len(self.vectors[0])):
            self.vectors[0][i] = 0.5
            self.vectors[self.height - 1][i] = 0.3


    def sharpen(self, value): 
        for i in range(len(self.vectors)):
            for j in range(len(self.vectors[0])):
                if (self.vectors[i][j] < 0.5):
                    self.vectors[i][j] -= value
                else:
                    self.vectors[i][j] += value

    def grain(self, value):
        for i in range(len(self.vectors)):
            for j in range(len(self.vectors[0])):
                if (random.randint(0,1) == 0):
                    if (random.randint(0, 1) == 0):
                        if (self.vectors[i][j] + value <= 1.5):
                            self.vectors[i][j] += value
                    else:
                        if (self.vectors[i][j] - value >= 0):
                            self.vectors[i][j] -= value

    def clear_vectors(self):
        # set all values in vectors to 0
        for i in range(len(self.vectors)):
            for j in range(len(self.vectors[0])):
                self.vectors[i][j] = 0.0


    def get_max(self):
        maxi = 0.0
        for i in range(len(self.vectors)):
            for j in range(len(self.vectors[0])):
                if (self.vectors[i][j] > maxi):
                    maxi = self.vectors[i][j]
        return maxi


    def get_min(self):
        mini = 5.0
        for i in range(len(self.vectors)):
            for j in range(len(self.vectors[0])):
                if (self.vectors[i][j] < mini):
                    mini = self.vectors[i][j]
        return mini


    def print_vectors(self): 
        # print board with coordinates
        screen = ''
   
        # draw Y coordinates
        for i in range(self.height):
            for j in range(self.width):
                value = str(round(self.vectors[i][j], 2))
                if (len(value) == 1): 
                    screen += value + '    '
                elif (len(value) == 2):
                    screen += value + '   '
                elif (len(value) == 3):
                    screen += value + '  '
                else:
                    screen += value + ' '
                    
        screen += '\n'
        print(screen)


    def get_color(self, value):
        # return a color based on input value
        COL1 = '[48;5;232m'
        COL2 = '[48;5;234m'
        COL3 = '[48;5;236m'
        COL4 = '[48;5;238m'
        COL5 = '[48;5;240m'
        COL6 = '[48;5;242m'
        COL7 = '[48;5;244m'
        COL8 = '[48;5;246m'
        COL9 = '[48;5;248m'
        COL10 = '[48;5;250m'
        COL11 = '[48;5;252m'
        COL12 = '[48;5;254m'
        COL13 = '[48;5;15m'
        COL14 = '[48;5;231m'
        COL15 = '[48;5;195m'
        COL16 = '[48;5;159m'
        COL17 = '[48;5;123m'
        COL18 = '[48;5;87m'
        COL19 = '[48;5;51m'
        '''
        COL1 = '[48;5;87m'
        COL2 = '[48;5;123m'
        COL3 = '[48;5;159m'
        COL4 = '[48;5;195m'
        COL5 = '[48;5;231m'
        COL6 = '[48;5;255m'
        COL7 = '[48;5;252m'
        COL8 = '[48;5;249m'
        COL9 = '[48;5;246m'
        COL10 = '[48;5;243m'
        COL11 = '[48;5;240m'
        COL12 = '[48;5;237m'
        COL13 = '[48;5;234m'
        COL14 = '[48;5;232m'
        COL15 = '[48;5;53m'
        COL16 = '[48;5;90m'
        COL17 = '[48;5;127m'
        COL18 = '[48;5;164m'
        COL19 = '[48;5;201m'
        '''

        if (0 <= value < 0.075):
            return COL1
        elif (0.075 <= value < 0.150):
            return COL2
        elif (0.150 <= value < 0.225):
            return COL3
        elif (0.225 <= value < 0.300):
            return COL4
        elif (0.300 <= value < 0.375):
            return COL5
        elif (0.375 <= value < 0.445):
            return COL6
        elif (0.445 <= value < 0.525):
            return COL7
        elif (0.525 <= value < 0.600):
            return COL8
        elif (0.600 <= value < 0.675):
            return COL9
        elif (0.675 <= value < 0.750):
            return COL10
        elif (0.750 <= value < 0.825):
            return COL11
        elif (0.825 <= value < 0.900):
            return COL12
        elif (0.900 <= value < 1.050):
            return COL13
        elif (1.050 <= value < 1.125):
            return COL14
        elif (1.125 <= value < 1.200):
            return COL15
        elif (1.200 <= value < 1.275):
            return COL16
        elif (1.275 <= value < 1.345):
            return COL17
        elif (1.345 <= value < 1.425):
            return COL18 
        elif (1.425 <= value < 1.500):
            return COL19
        else:
            return COL1

       
    def print_board(self):
        # print board with coordinates and colors
        screen = ''
        ESC = '\x1b'

        for i in range(self.height):
            screen += '\n'
            for j in range(self.width): 
                value = self.vectors[i][j] 
                color = self.get_color(value)
                #print(f'value -> {value}, color -> {color}')
                screen += ESC + self.get_color(value) + '  '
                    
        print(screen)
