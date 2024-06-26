import random
import sys

class Tartress:
    def __init__(self, width=36, height=24, difficulty=2):
        self.difficulty = difficulty
        self.width = width
        self.height = height
        self.board = [[0] * self.width for i in range(self.height)]
        self.revealed = [[0] * self.width for i in range(self.height)]
        self.flags = [[0] * self.width for i in range(self.height)]
        self.populate_bombs()
        sys.setrecursionlimit(10**6)

        self.cursor_x = 17
        self.cursor_y = 12


    def get_flag_matrix(self, y, x):
        # return a matrix of all the surrounding cells
        matrix = [[self.flags[y-1][x-1], self.flags[y-1][x], self.flags[y-1][x+1]],
                  [self.flags[y-1][x-1], self.flags[y-1][x], self.flags[y-1][x+1]],
                  [self.flags[y-1][x-1], self.flags[y-1][x], self.flags[y-1][x+1]]]

        return matrix


    def count_bombs(self):
        # count the number of bombs on the board
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if (self.board[i][j] == 9):
                    count += 1

        return count


    def count_flags(self, y, x):
        # count the number of 
        count = 0

        # if top left corner
        if (y == 0 and x == 0):
            if (self.flags[y][x+1] == 1):
                count += 1
            if (self.flags[y+1][x] == 1):
                count += 1
            if (self.flags[y+1][x+1] == 1):
                count += 1
        
        # if top right corner
        elif (y == 0 and x == self.width-1):
            if (self.flags[y][x-1] == 1):
                count += 1
            if (self.flags[y+1][x] == 1):
                count += 1
            if (self.flags[y+1][x-1] == 1):
                count += 1

        # if bottom left corner
        elif (y == self.height-1 and x == 0):
            if (self.flags[y][x+1] == 1):
                count += 1
            if (self.flags[y-1][x] == 1):
                count += 1
            if (self.flags[y-1][x+1] == 1):
                count += 1

        # if bottom right corner
        elif (y == self.height-1 and x == self.width-1):
            if (self.flags[y][x-1] == 1):
                count += 1
            if (self.flags[y-1][x] == 1):
                count += 1
            if (self.flags[y-1][x-1] == 1):
                count += 1

        # if on top edge
        elif (y == 0 and 0 < x < self.width-1):
            if (self.flags[y][x-1] == 1):
                count += 1
            if (self.flags[y][x+1] == 1):
                count += 1
            if (self.flags[y+1][x-1] == 1):
                count += 1
            if (self.flags[y+1][x] == 1):
                count += 1
            if (self.flags[y+1][x+1] == 1):
                count += 1

        # if on left edge
        elif (0 < y < self.height-1 and x == 0):
            if (self.flags[y-1][x] == 1):
                count += 1
            if (self.flags[y-1][x+1] == 1):
                count += 1
            if (self.flags[y][x+1] == 1):
                count += 1
            if (self.flags[y+1][x] == 1):
                count += 1
            if (self.flags[y+1][x+1] == 1):
                count += 1
        
        # if on bottom edge
        elif (y == self.height-1 and 0 < x < self.width-1):
            if (self.flags[y-1][x-1] == 1):
                count += 1
            if (self.flags[y-1][x] == 1):
                count += 1
            if (self.flags[y-1][x+1] == 1):
                count += 1
            if (self.flags[y][x-1] == 1):
                count += 1
            if (self.flags[y][x+1] == 1):
                count += 1
 
        # if on right edge
        elif (0 < y < self.height-1 and x == self.width-1):
            if (self.flags[y-1][x] == 1):
                count += 1
            if (self.flags[y-1][x-1] == 1):
                count += 1
            if (self.flags[y][x-1] == 1):
                count += 1
            if (self.flags[y+1][x] == 1):
                count += 1
            if (self.flags[y+1][x-1] == 1):
                count += 1
        
        # if in middle
        else:
            if (self.flags[y-1][x-1] == 1):
                count += 1
            if (self.flags[y-1][x] == 1):
                count += 1
            if (self.flags[y-1][x+1] == 1):
                count += 1
            if (self.flags[y][x-1] == 1):
                count += 1
            if (self.flags[y][x+1] == 1):
                count += 1
            if (self.flags[y+1][x-1] == 1):
                count += 1
            if (self.flags[y+1][x] == 1):
                count += 1
            if (self.flags[y+1][x+1] == 1):
                count += 1

        return count


    
    def check_win(self):
        flags = []
        bombs = []
        for i in range(self.height):
            for j in range(self.width):
                if (self.flags[i][j] == 1):
                    flags.append(1)
                else:
                    flags.append(0)

                if (self.board[i][j] == 9):
                    bombs.append(1)
                else:
                    bombs.append(0)

        return flags == bombs


    def check_revealed(self):
        # check that the entire board is revealed
        for i in range(self.height):
            for j in range(self.width):
                if (self.revealed[i][j] == 0):
                    return False

        return True


    def start_game(self, y, x):
        # start the game with the first click
        for i in range(y-2, y+2):
            for j in range(x-2, x+2):
                self.board[i][j] = 0 

        self.populate_counts()
        self.reveal(y, x)


    def reveal(self, y, x):
        # given a coordinate, if it is a 0, recursively reveal 0's
        if (y < 0 or y > self.height-1 or x < 0 or x > self.width-1 or self.revealed[y][x] == 1):
            return

        self.revealed[y][x] = 1

        if (self.board[y][x] != 0):
            return

        else:
            self.reveal(y-1, x)
            self.reveal(y-1, x+1)
            self.reveal(y-1, x-1)
            self.reveal(y, x-1)
            self.reveal(y, x+1)
            self.reveal(y+1, x)
            self.reveal(y+1, x+1)
            self.reveal(y+1, x-1)

    def populate_bombs(self):
        # based on the difficulty, place bombs into the board
        bombs = [9 for i in range((self.difficulty + 1) * 15 + 40)]

        while (len(bombs) > 0):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if (self.board[y][x] != 9):
                self.board[y][x] = bombs.pop()


    def count_neighbors(self, y, x, item):
        # given a coordinate, count the number of surrounding bombs
        count = 0

        # if top left corner
        if (y == 0 and x == 0):
            if (self.board[y][x+1] == item):
                count += 1
            if (self.board[y+1][x] == item):
                count += 1
            if (self.board[y+1][x+1] == item):
                count += 1
        
        # if top right corner
        elif (y == 0 and x == self.width-1):
            if (self.board[y][x-1] == item):
                count += 1
            if (self.board[y+1][x] == item):
                count += 1
            if (self.board[y+1][x-1] == item):
                count += 1

        # if bottom left corner
        elif (y == self.height-1 and x == 0):
            if (self.board[y][x+1] == item):
                count += 1
            if (self.board[y-1][x] == item):
                count += 1
            if (self.board[y-1][x+1] == item):
                count += 1

        # if bottom right corner
        elif (y == self.height-1 and x == self.width-1):
            if (self.board[y][x-1] == item):
                count += 1
            if (self.board[y-1][x] == item):
                count += 1
            if (self.board[y-1][x-1] == item):
                count += 1

        # if on top edge
        elif (y == 0 and 0 < x < self.width-1):
            if (self.board[y][x-1] == item):
                count += 1
            if (self.board[y][x+1] == item):
                count += 1
            if (self.board[y+1][x-1] == item):
                count += 1
            if (self.board[y+1][x] == item):
                count += 1
            if (self.board[y+1][x+1] == item):
                count += 1

        # if on left edge
        elif (0 < y < self.height-1 and x == 0):
            if (self.board[y-1][x] == item):
                count += 1
            if (self.board[y-1][x+1] == item):
                count += 1
            if (self.board[y][x+1] == item):
                count += 1
            if (self.board[y+1][x] == item):
                count += 1
            if (self.board[y+1][x+1] == item):
                count += 1
        
        # if on bottom edge
        elif (y == self.height-1 and 0 < x < self.width-1):
            if (self.board[y-1][x-1] == item):
                count += 1
            if (self.board[y-1][x] == item):
                count += 1
            if (self.board[y-1][x+1] == item):
                count += 1
            if (self.board[y][x-1] == item):
                count += 1
            if (self.board[y][x+1] == item):
                count += 1
 
        # if on right edge
        elif (0 < y < self.height-1 and x == self.width-1):
            if (self.board[y-1][x] == item):
                count += 1
            if (self.board[y-1][x-1] == item):
                count += 1
            if (self.board[y][x-1] == item):
                count += 1
            if (self.board[y+1][x] == item):
                count += 1
            if (self.board[y+1][x-1] == item):
                count += 1
        
        # if in middle
        else:
            if (self.board[y-1][x-1] == item):
                count += 1
            if (self.board[y-1][x] == item):
                count += 1
            if (self.board[y-1][x+1] == item):
                count += 1
            if (self.board[y][x-1] == item):
                count += 1
            if (self.board[y][x+1] == item):
                count += 1
            if (self.board[y+1][x-1] == item):
                count += 1
            if (self.board[y+1][x] == item):
                count += 1
            if (self.board[y+1][x+1] == item):
                count += 1

        return count


    def populate_counts(self):
        # populate the board with the number of surrounding tiles which are bombs
        for i in range(self.height):
            for j in range(self.width):
                if (self.board[i][j] != 9):
                    self.board[i][j] = self.count_neighbors(i, j, 9)


    def print_board(self):
        # print the board
        ESC = '\x1b'
        TEXT = '[38;5;'
        BACKGROUND = '[48;5;'

        screen = ESC + '' 
        for i in range(self.height):
            screen += '\n'
            for j in range(self.width):

                if (i == self.cursor_y and j == self.cursor_x):
                    screen += ESC + BACKGROUND + '40m'

                elif (self.revealed[i][j] == 0):
                    screen += ESC + BACKGROUND + '235m'

                else:
                    if (self.board[i][j] == 0):
                        screen += ESC + BACKGROUND + '240m'
                    else:
                        screen += ESC + BACKGROUND + '237m'

                screen += ESC + TEXT + f'{self.board[i][j]}m{self.board[i][j]} ' 

        print(screen + '\n')


    def print_play_board(self, option=0):
        # print the board
        ESC = '\x1b'
        TEXT = '[38;5;'
        BACKGROUND = '[48;5;'

        screen = ESC + BACKGROUND + '245m'
        for k in range(self.width):
            screen += '  '
        for i in range(self.height):
            screen += '\n  '

            for j in range(self.width):
                # if cursor
                if (i == self.cursor_y and j == self.cursor_x):
                    # if space is a flag
                    if (self.flags[i][j] == 1):
                        screen += ESC + BACKGROUND + '40m'
                        screen += ESC + TEXT + '15mF '

                    # if space is revealed
                    elif (self.revealed[i][j] == 1 and self.board[i][j] != 0):
                        screen += ESC + BACKGROUND + '40m'
                        screen += ESC + TEXT + f'15m{self.board[i][j]} '

                    # if space is not flag or revealed
                    else:
                        screen += ESC + BACKGROUND + '40m  '

                else:
                        
                    # if space is flagged
                    if (self.flags[i][j] == 1):
                        screen += ESC + BACKGROUND + '196m' 
                        screen += ESC + TEXT + '15mF '

                    # if space NOT flagged
                    else:
                        # if revealed 
                        if (self.revealed[i][j] == 1):
                            screen += ESC + BACKGROUND + '238m'
                            # if space == 0
                            if (self.board[i][j] == 0):
                                screen += ESC + BACKGROUND + '240m  '
                            
                            # if space NOT == 0
                            else:
                                screen += ESC + TEXT + f'{self.board[i][j]}m{self.board[i][j]} '

                        # if NOT revealed
                        else:
                            screen += ESC + BACKGROUND + '236m  '

            screen += ESC + BACKGROUND + '245m  '

        screen += ESC + BACKGROUND + '245m'
        for k in range(self.width):
            screen += '  '

        print(screen + '\n')



