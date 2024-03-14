import os
import sys
import random 
import time
import keyboard

class Paint():
    def __init__(self, width=51, height=57): 
        self.width = width
        self.height = height
        self.board = [['153m'] * self.width for i in range(self.height)]    
        self.file_name = ''

        # load colors into board
        count = 0
        for i in range(1, height - 2):
            self.board[i][2] = f'{i - 2}m'
            count += 1
        
        for i in range(1, height - 2):
            self.board[i][3] = f'{i + count - 2}m'
            count += 1

        for i in range(1, height - 2):
            self.board[i][4] = f'{i + count - 2}m'
            count += 1

        for i in range(1, height - 2):
            if (i + count < 256):
                self.board[i][5] = f'{i + count - 2}m'
                count += 1

        self.cursor = [width // 2, height // 2]
        self.curr_color = '213m' 
        self.setting = 'p' 


    def print_board(self): 
        # define ansi espape codes
        ESC = '\x1b'
        BEGIN =  '[48;5;'
        CURSOR = '[38;5;231m'
        # declare string for printing self.board
        screen = ''
        
        for i in range(self.height):
            screen += '\n'
            for j in range(self.width - 5):
                
                # if cursor 
                if (self.cursor[0] == i and self.cursor[1] == j and j < 6):
                    screen += ESC + BEGIN + self.board[i][j] + '  ' 

                elif (self.cursor[0] == i and self.cursor[1] == j):
                    screen += ESC + BEGIN + self.curr_color + '  ' 

                elif (self.cursor[0] == i and self.cursor[1] - 1 == j):
                    # set text color 
                    screen += ESC + '[38;5;231m'
                    board_color = self.board[i][j]
                    screen += ESC + BEGIN + board_color + ' -'

                elif (self.cursor[0] == i and self.cursor[1] + 1 == j):
                    # set text color 
                    screen += ESC + '[38;5;231m'
                    board_color = self.board[i][j]
                    screen += ESC + BEGIN + board_color + '- '

                else:
                    # if border pixel
                    if (i == self.height - 1 or j == 0):
                        screen += ESC + BEGIN + '145m' + '  '
                    elif (i == 0 or j == self.width - 1):
                        screen += ESC + BEGIN + '247m' + '  '
                    elif (i == 1 or j == self.width - 2):
                        screen += ESC + BEGIN + '246m' + '  '
                    elif (i == self.height - 2 or j == 1):
                        screen += ESC + BEGIN + '246m' + '  '
                    else:
                        screen += ESC + BEGIN + self.board[i][j] + '  '

        print(screen)
        print()


'''

    def read_file(self, file_name):
        # TODO -> implement file read function
        self.file_name = file_name
        



    def write_file(self, file_name):
        file_name += '.kbb'
        write = []
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
                
        
    '''             
if __name__ == '__main__':
    paint = Paint()
 
    game_loop = True
    # begin game loop
    while (game_loop):
        paint.print_board()
        time.sleep(0.09)

        if keyboard.is_pressed("w"):
            paint.cursor[0] -= 1
        
        if keyboard.is_pressed("a"):
            #if (paint.cursor[1] > 6):
            paint.cursor[1] -= 1

        if keyboard.is_pressed("s"):
            paint.cursor[0] += 1

        if keyboard.is_pressed("d"):
            paint.cursor[1] += 1

        # activate
        if keyboard.is_pressed("v"):
            paint.board[paint.cursor[0]][paint.cursor[1]] = paint.curr_color

        # select color
        if keyboard.is_pressed("g"):
            paint.curr_color = paint.board[paint.cursor[0]][paint.cursor[1]]

'''                     
        if keyboard.is_pressed(":"):
            print('  OPTIONS')
            print('   0 )  open')
            if (paint.file_name == ''):
                print('   1 )  save as')
            else:
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
                game_loop = False


            elif (option == ':1'):
                # write file
                print('\nEnter File Name: ', end='')
                file_name = input()
                paint.write_file(f'{file_name}.kbb')
                


'''
