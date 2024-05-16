import random

class Moisture():

    def __init__(self, width=51, height=56):
        self.test = 'hello'
        self.width = width
        self.height = height
        self.board = [[0] * self.width for i in range(self.height)]


    def check_cell(self, y, x):
        # check if the count of the cells surrounding current cell is greater than the current cell
        count = 0
        if (self.board[y - 1][x - 1] > 0):
            count += 1
        if (self.board[y - 1][x] > 0):
            count += 1
        if (self.board[y - 1][x + 1] > 0):
            count += 1
        if (self.board[y][x - 1] > 0):
            count += 1
        if (self.board[y][x + 1] > 0):
            count += 1
        if (self.board[y + 1][x - 1] > 0):
            count += 1
        if (self.board[y + 1][x] > 0):
            count += 1
        if (self.board[y + 1][x + 1] > 0):
            count += 1
        
        # do something 
        if (count > self.board[y][x]):
            return False
        else:
            return True


    def iterate_board(self):
        for i in range(self.height - 2, 1, -1):
            for j in range(1, self.width - 2):
                if (self.board[i][j] >= 7):
                    self.board[i + 1][j] = self.board[i][j] + 1

                    row = i 
                    while (self.board[row][j] >= 1):
                        self.board[row][j] -= 1
                        row -= 1
        
        for j in range(0, self.width - 1):
            self.board[self.height - 1][j] = 0
                     
    def insert_droplet(self):
        # insert a droplet on a random location on the board
        x = random.randint(1, self.width - 2)
        y = random.randint(1, self.height - 2)
        if (self.board[y][x] >= 9):
            return 
        else:
            self.board[y][x] += 1


    def dry_board(self):
        for i in range(self.height):
            for j in range(self.width):
                if (self.board[i][j] >= 1):
                    if (self.check_cell(i, j) and self.board[i][j] >= 1):
                        self.board[i][j] -= 1  




    def print_board(self):
        # print the board
        ESC = '\x1b'
        TEXT = '[38;5;167m' 
        OTHER = '[38;5;33m' 
        ZERO = '[48;5;234m'
        ONE = '[48;5;235m'
        TWO = '[48;5;236m'
        THREE = '[48;5;237m'
        FOUR = '[48;5;238m'
        FIVE = '[48;5;239m'
        SIX = '[48;5;240m'
        SEVEN = '[48;5;241m'
        EIGHT = '[48;5;242m'

        screen = ''
        for i in range(self.height):
            screen += '\n'
            for j in range(self.width): 
                if (self.board[i][j] == 0):
                    screen += ESC + ZERO + '  '
                elif (self.board[i][j] == 1):
                    screen += ESC + ONE + '  '
                elif (self.board[i][j] == 2):
                    screen += ESC + TWO + '  '
                elif (self.board[i][j] == 3):
                    screen += ESC + THREE + '  '
                elif (self.board[i][j] == 4):
                    screen += ESC + FOUR + '  '
                elif (self.board[i][j] == 5):
                    screen += ESC + FIVE + '  '
                elif (self.board[i][j] == 6):
                    screen += ESC + SIX + '  '
                elif (self.board[i][j] == 7):
                    screen += ESC + SEVEN + '  '
                elif (self.board[i][j] == 8):
                    screen += ESC + EIGHT + '  '
                
            """
            for j in range(self.width): 
                if (self.board[i][j] == 0):
                    screen += ESC + ZERO + f' {self.board[i][j]}'
                elif (self.board[i][j] == 1):
                    screen += ESC + ONE + f' {self.board[i][j]}'
                elif (self.board[i][j] == 2):
                    screen += ESC + TWO + f' {self.board[i][j]}'
                elif (self.board[i][j] == 3):
                    screen += ESC + THREE + f' {self.board[i][j]}'
                elif (self.board[i][j] == 4):
                    screen += ESC + FOUR + f' {self.board[i][j]}'
                elif (self.board[i][j] == 5):
                    screen += ESC + FIVE + f' {self.board[i][j]}'
                elif (self.board[i][j] == 6):
                    screen += ESC + SIX + f' {self.board[i][j]}'
                elif (self.board[i][j] == 7):
                    screen += ESC + SEVEN + f' {self.board[i][j]}'
                elif (self.board[i][j] == 8):
                    screen += ESC + EIGHT + f' {self.board[i][j]}'

            """

        print(screen)

    

    
