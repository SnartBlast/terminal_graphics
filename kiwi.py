import random
import math 

class Kiwi():
    # Kiwi's Noise Generator, based off of Perlin Noise
    def __init__(self, width, height):
        self.width = width
        self.height = height 
        self.vectors = [[0] * (self.width) for i in range(self.height)]
    
    
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

    def clear_vectors(self):
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
        COL1 = '[48;5;28m'
        COL2 = '[48;5;64m'
        COL3 = '[48;5;100m'
        COL4 = '[48;5;136m'
        COL5 = '[48;5;172m'
        COL6 = '[48;5;208m'
        COL7 = '[48;5;209m'
        COL8 = '[48;5;210m'
        COL9 = '[48;5;211m'
        COL10 = '[48;5;212m'
        COL11 = '[48;5;213m'
        COL12 = '[48;5;177m'
        COL13 = '[48;5;141m'
        COL14 = '[48;5;105m'
        COL15 = '[48;5;69m'
        COL16 = '[48;5;33m'
        COL17 = '[48;5;32m'
        COL18 = '[48;5;31m'
        COL19 = '[48;5;30m'


        if (0 <= value < 0.20):
            return COL1
        elif (0.20 <= value < 0.40):
            return COL2
        elif (0.40 <= value < 0.60):
            return COL3
        elif (0.60 <= value < 0.80):
            return COL4
        elif (1.00 <= value < 1.20):
            return COL5
        elif (1.20 <= value < 1.40):
            return COL6
        elif (1.40 <= value < 1.60):
            return COL7
        elif (1.60 <= value < 1.80):
            return COL8
        elif (1.80 <= value < 2.00):
            return COL9
        elif (2.00 <= value < 2.20):
            return COL10
        elif (2.20 <= value < 2.40):
            return COL11 
        elif (2.40 <= value < 2.60):
            return COL12
        elif (2.60 <= value < 2.80):
            return COL13 
        elif (2.80 <= value < 3.00):
            return COL14 
        elif (3.00 <= value < 3.20):
            return COL15 
        elif (3.20 <= value < 3.40):
            return COL16 
        elif (3.40 <= value < 3.60):
            return COL17 
        elif (3.60 <= value < 3.80):
            return COL18 
        else:
            return COL19


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
    
    

          
    


            


                
                 



