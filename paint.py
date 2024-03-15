import os
import sys
import random 
import time
import keyboard

class Paint():
    # W, A, S, D = move cursor
    # Up, Down, Left, Right = move preview cursor

    # C = open palette
    # G = select color
    # V = place color
    # F = fill 

    def __init__(self, width=51, height=57): 
        # board data
        self.width = width
        self.height = height
        self.board = [['189m'] * self.width for i in range(self.height)]    
        self.canvas = [['  '] * self.width for i in range(self.height)] 
        self.cursor = [width // 2, height // 2]
        self.curr_color = '213m' 

        # preview data
        self.preview_cursor = [width // 2, height // 2]
        self.preview_color = '26m'
        self.show_preview = False
        self.get_timer = 0

        # file and settings data
        self.file_name = ''
        self.last_moved = 0
        self.setting = 'p' 

        # load colors into board
        for i in range(1, 55):
            self.board[i][1] = f'{i + 15}m'
        for i in range(1, 55):
            self.board[i][2] = f'{i + 51}m'
        for i in range(1, 55):
            self.board[i][3] = f'{i + 87}m'
        for i in range(1, 55):
            self.board[i][4] = f'{i + 123}m'
        for i in range(1, 55):
            self.board[i][5] = f'{i + 159}m'
        for i in range(1, 37):
            self.board[i][6] = f'{i + 195}m'
        for i in range(37, 55):
            self.board[i][6] = f'{i + 197}m'
        for i in range(55, 61):
            self.board[55][i - 54] = f'{i + 195}m'

        # build borders
        for i in range(height):
            self.board[i][0] = '250m'
            self.board[i][7] = '250m'
            self.board[i][8] = '250m'
            self.board[i][width - 2] = '250m'
            self.board[i][width - 1] = '250m'

        for i in range(width):
            self.board[0][i] = '250m'
            self.board[height - 1][i] = '250m'
        
        # build canvas highlighting
        for i in range(9, width - 2):
            self.board[height - 2][i] = '254m'
            self.board[1][i] = '248m'

        for i in range(2, height - 2):
            self.board[i][8] = '249m'
            self.board[i][width - 2] = '253m'


    def print_board(self): 
        # define ansi espape codes
        ESC = '\x1b'
        BEGIN =  '[48;5;'
        CURSOR = '[38;5;231m'
        screen = ''
        screen += ESC + CURSOR

        # get preview coords
        x = self.preview_cursor[0]
        y = self.preview_cursor[1]
        
        for i in range(self.height):
            screen += '\n'
            for j in range(self.width):
                # show cursor
                if (self.cursor[0] == i and self.cursor[1] == j):
                    # if cursor is in color select mode
                    if (j < 7):
                        screen += ESC + BEGIN + self.board[i][j] + '()' 
                    
                    # check idle cursor
                    else:
                        if (self.last_moved > 30):
                            if (10 < self.last_moved % 20 < 20):
                                screen += ESC + '[38;5;16m'

                        screen += ESC + BEGIN + self.curr_color + '()'

                # show preview cursor
                elif (self.show_preview and x == i and y == j):
                    screen += ESC + BEGIN + self.preview_color + '  '
                elif (self.show_preview and x == i - 1 and y == j - 1):
                    screen += ESC + BEGIN + self.preview_color + '  '
                elif (self.show_preview and x == i - 1 and y == j):
                    screen += ESC + BEGIN + self.preview_color + '  '
                elif (self.show_preview and x == i - 1 and y == j + 1):
                    screen += ESC + BEGIN + self.preview_color + '  '
                elif (self.show_preview and x == i and y == j - 1):
                    screen += ESC + BEGIN + self.preview_color + '  '
                elif (self.show_preview and x == i and y == j):
                    screen += ESC + BEGIN + self.preview_color + '  '
                elif (self.show_preview and x == i and y == j + 1):
                    screen += ESC + BEGIN + self.preview_color + '  '
                elif (self.show_preview and x == i + 1 and y == j - 1):
                    screen += ESC + BEGIN + self.preview_color + '  '
                elif (self.show_preview and x == i + 1 and y == j):
                    screen += ESC + BEGIN + self.preview_color + '  '
                elif (self.show_preview and x == i + 1 and y == j + 1):
                    screen += ESC + BEGIN + self.preview_color + '  '

                # show the rest of the board
                else:
                    screen += ESC + BEGIN + self.board[i][j] + '  '

        print(screen)
        print()


    def read_file(self, file_name):
        # TODO -> implement file read function
        self.file_name = file_name
        fle = open(f'{file_name}')
        
        # parse file line by line
        for i, line in enumerate(fle):
            line = line.split(',')[:-1]
            
            for j, item in enumerate(line):
                self.board[i][j] = item
         

        
    def write_file(self, file_name):
        write = []
        if (self.file_name == ''):
            file_name += '.kbb'
        if '.kbb' not in file_name:
            file_name += '.kbb'

        self.file_name = file_name

        # create file line container
        for i, line in enumerate(self.board):
            text = ''
            for item in line: 
                text += item + ','

            text += ' END\n'
            write.append(text)

        # if file is not already in CWD
        if (not os.path.isfile(file_name)):
            # create new file 
            fle = open(file_name, 'x')
            for item in write:
                fle.write(item)
            fle.close()

        # if file is already in the CWD
        else:
            fle = open(file_name, 'w')
            for item in write:
                fle.write(item)
            fle.close() 


    def fill(self, y, x, color, count):
        # recursively fill shapes
        if (1 < y < self.height - 2 and 8 < x < self.width - 2):
            self.board[y][x] = color

            # check if adjacent cells are correct color
            if (self.board[y - 1][x] != color):
                self.fill(y - 1, x, color, count + 1)
            if (self.board[y + 1][x] != color):
                self.fill(y + 1, x, color, count + 1)
            if (self.board[y][x - 1] != color):
                self.fill(y, x - 1, color, count + 1)
            if (self.board[y][x + 1] != color):
                self.fill(y, x + 1, color, count + 1)


    def get_color(self):
        return self.board[self.cursor[0]][self.cursor[1]]


if __name__ == '__main__':

    paint = Paint() 
    game_loop = True

    # begin game loop
    while (game_loop):
        paint.print_board()
        time.sleep(0.09)
        paint.last_moved += 1
        paint.get_timer += 1

        # Move paint cursor up
        if keyboard.is_pressed("w"):
            paint.last_moved = 0
            if (paint.setting == 'c'):
                if (paint.cursor[0] > 1):
                    paint.cursor[0] -= 1
                    paint.preview_color = paint.get_color()
            else:
                if (paint.cursor[0] > 2):
                    paint.cursor[0] -= 1
        
        # Move paint cursor left
        if keyboard.is_pressed("a"):
            paint.last_moved = 0
            if (paint.setting == 'c'):
                if (paint.cursor[1] > 1):
                    paint.cursor[1] -= 1
                    paint.preview_color = paint.get_color()
            else:
                if (paint.cursor[1] > 9):
                    paint.cursor[1] -= 1

        # Move paint cursor down
        if keyboard.is_pressed("s"):
            paint.last_moved = 0
            if (paint.setting == 'c'):
                if (paint.cursor[0] < paint.height - 2):
                    paint.cursor[0] += 1
                    paint.preview_color = paint.get_color()
            else:
                if (paint.cursor[0] < paint.height - 3):
                    paint.cursor[0] += 1

        # Move paint cursor right
        if keyboard.is_pressed("d"):
            paint.last_moved = 0
            if (paint.setting == 'c'):
                if (paint.cursor[1] < 6):
                    paint.cursor[1] += 1
                    paint.preview_color = paint.get_color()
            else:
                if (paint.cursor[1] < paint.width - 3):
                    paint.cursor[1] += 1

        ################################################################

        # Move preview cursor up
        if keyboard.is_pressed("up"):
            if (paint.preview_cursor[0] > 3):
                paint.preview_cursor[0] -= 1
        
        # Move preview cursor left
        if keyboard.is_pressed("left"):
            if (paint.preview_cursor[1] > 10):
                paint.preview_cursor[1] -= 1

        # Move preview cursor down
        if keyboard.is_pressed("down"):
            if (paint.preview_cursor[0] < paint.height - 4):
                paint.preview_cursor[0] += 1

        # Move preview cursor right
        if keyboard.is_pressed("right"):
            if (paint.preview_cursor[1] < paint.width - 4):
                paint.preview_cursor[1] += 1

        ################################################################

        # place color
        if keyboard.is_pressed("v"):
            if (paint.setting != 'c'):
                paint.board[paint.cursor[0]][paint.cursor[1]] = paint.curr_color
            
            # select preview color
            else:
                paint.preview_color = paint.board[paint.cursor[0]][paint.cursor[1]]

        # select color
        if keyboard.is_pressed("g"):
            if (paint.get_timer > 5):  
                paint.get_timer = 0            
                paint.curr_color = paint.board[paint.cursor[0]][paint.cursor[1]]
                if paint.setting == 'c':
                    paint.cursor[0] = paint.height // 2
                    paint.cursor[1] = paint.width // 2 + 4
                    paint.setting = 'p'
                    paint.show_preview = False

        # open palette
        if keyboard.is_pressed("c"):
            paint.show_preview = True
            paint.setting = 'c'
            paint.cursor[0] = paint.height // 2
            paint.cursor[1] = 3

        # fill shape
        if keyboard.is_pressed("f"):
            if (paint.setting != 'c'):
                paint.fill(paint.cursor[0], paint.cursor[1], paint.curr_color, 0)
            
        ################################################################
    
        if keyboard.is_pressed(":"):
            print('  OPTIONS')
            print('   0 )  open')
            print('   1 )  save')
            print('   2 )  save as')

            # get option as input
            print('\n  Enter Selection: ', end='')
            option = input()
            
            if (option == ':0'):
                # display files and get input 
                # I got this next line from stack overflow btw! No credit for this plz!
                files = [f for f in os.listdir('.') if os.path.isfile(f)]
                count = 0
                file_list = []
                for item in files:
                    if '.kbb' in item:
                        file_list.append(item)
                        print(f'   {count} ) {item}')
                        count += 1

                print('\n  Enter Selection: ', end='')
                option = int(input())
                paint.read_file(file_list[option])


            elif (option == ':1'):
                # write file
                if (paint.file_name != ''):
                    paint.write_file(f'{paint.file_name}')
                else:
                    print('\nEnter File Name: ', end='')
                    file_name = input()
                    paint.write_file(f'{file_name}')

                print('\n\nFILE SUCCESSFULLY SAVED\n')
                time.sleep(1)

            elif (option == ':2'):
                # write file
                print('\nEnter File Name: ', end='')
                file_name = input()
                paint.write_file(f'{file_name}')




