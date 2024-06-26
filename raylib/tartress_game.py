import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
from tartress import Tartress
import keyboard
import time

'''
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

import requests



try:
    response = requests.get(f'https://geolocation-db.com/json/{IPAddr}&position=true').json()
    print(response)
except:
    print('Please connect to wifi! Ugh!')
'''
tartress = Tartress(36, 24, 3)
tartress.start_game(12, 17)
#tartress.print_board()

game_loop = True

while game_loop:
    if (tartress.check_win()):
        game_loop = False
        tartress.print_play_board(0)
        print('YOU WIN')

    tartress.print_play_board()

    # Move preview cursor up
    if keyboard.is_pressed("up"):
        tartress.cursor_y -= 1
    
    # Move preview cursor left
    if keyboard.is_pressed("left"):
        tartress.cursor_x -= 1

    # Move preview cursor down
    if keyboard.is_pressed("down"):
        tartress.cursor_y += 1

    # Move preview cursor right
    if keyboard.is_pressed("right"):
        tartress.cursor_x += 1

    if keyboard.is_pressed("f"):
        time.sleep(0.1)
        if (tartress.flags[tartress.cursor_y][tartress.cursor_x] == 1):
            tartress.flags[tartress.cursor_y][tartress.cursor_x] = 0

        else:
            tartress.flags[tartress.cursor_y][tartress.cursor_x] = 1



    if keyboard.is_pressed("space"):
        # if activate bomb
        if (tartress.board[tartress.cursor_y][tartress.cursor_x] == 9):
            game_loop = False
            tartress.print_play_board(1)
            print('GAME OVER')

        elif (tartress.count_flags(tartress.cursor_y, tartress.cursor_x) == tartress.board[tartress.cursor_y][tartress.cursor_x]):
            # reveal the rest of the items aruond the cursor

            reveal = tartress.get_flag_matrix(tartress.cursor_y, tartress.cursor_x)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (reveal[i+1][j+1] == 0):

                        if (0 <= tartress.cursor_y + i < tartress.height and 0 <= tartress.cursor_x + j < tartress.width):
                            tartress.reveal(tartress.cursor_y + i, tartress.cursor_x + j)
                        else:
                            tartress.reveal(tartress.cursor_y, tartress.cursor_x)

        else:
            tartress.reveal(tartress.cursor_y, tartress.cursor_x)

    time.sleep(0.1)










