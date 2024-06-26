import pyray
from graphics_2 import Graphics
from cube import Cube
from letters import Letters
from tartress import Tartress
import time

# raylib screen setup
WIDTH = 288 # 8 * 36
HEIGHT = 160 # 8 * 24
PIXEL_SIZE = 5
pyray.init_window(WIDTH * PIXEL_SIZE, HEIGHT * PIXEL_SIZE, 'Raylib Testing')
pyray.set_target_fps(30)

# tartress game setup
tartress = Tartress(WIDTH // 8, HEIGHT // 8, 3)
tartress.start_game(WIDTH // 8 // 2, HEIGHT // 8 // 2)
game_loop = True
show_bombs = 0

# letters setup
letters = Letters()

# define unique tartress symbols
cursor = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1]]

bomb = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]



def draw_letter(y, x, letter):
    # draw revealed letter to the screen
    COLOR_BACKGROUND_ZERO = (150, 150, 150, 255)
    COLOR_BACKGROUND_OTHER = (130, 130, 130, 255)
    ONE = (255, 0, 0, 255)
    TWO = (0, 255, 0, 255)
    THREE = (0, 0, 255, 255)
    FOUR = (255, 255, 0, 255)
    FIVE = (255, 0, 255, 255)
    SIX = (0, 255, 255, 255)
    SEVEN = (255, 100, 255, 255)
    COLORS = [COLOR_BACKGROUND_ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, (255, 255, 255, 255), COLOR_BACKGROUND_ZERO]

    if (letter == 0):
        pyray.draw_rectangle((x * PIXEL_SIZE * 8), (y * PIXEL_SIZE * 8), PIXEL_SIZE * 8, PIXEL_SIZE * 8, COLOR_BACKGROUND_ZERO)
        return

    else:
        pyray.draw_rectangle((x * PIXEL_SIZE * 8), (y * PIXEL_SIZE * 8), PIXEL_SIZE * 8, PIXEL_SIZE * 8, COLOR_BACKGROUND_ZERO)


    space_matrix = letters.word_matrix(str(letter))

    for i in range(len(space_matrix)):
        for j in range(len(space_matrix[i])):
            if (space_matrix[i][j] == 1):
                pyray.draw_rectangle((x * PIXEL_SIZE * 8) + j * PIXEL_SIZE, (y * PIXEL_SIZE * 8) + i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE, COLORS[letter])

    pyray.draw_rectangle(x * PIXEL_SIZE * 8, y * PIXEL_SIZE * 8, 8 * PIXEL_SIZE, 1 * PIXEL_SIZE, (200, 200, 200, 255))
    pyray.draw_rectangle(x * PIXEL_SIZE * 8, y * PIXEL_SIZE * 8, 1 * PIXEL_SIZE, 8 * PIXEL_SIZE, (200, 200, 200, 255))
    pyray.draw_rectangle((x * PIXEL_SIZE * 8) + (PIXEL_SIZE * 7), y * PIXEL_SIZE * 8, 1 * PIXEL_SIZE, 8 * PIXEL_SIZE, (130, 130, 130, 255))
    pyray.draw_rectangle((x * PIXEL_SIZE * 8), y * PIXEL_SIZE * 8 + (PIXEL_SIZE * 7), 8 * PIXEL_SIZE, 1 * PIXEL_SIZE, (130, 130, 130, 255))


def draw_item(y, x, choice):
    space_matrix = None
    COLOR = None
    COLOR_BACKGROUND_OTHER = (110, 110, 110, 255)
    
    if (choice == 0):
        space_matrix = letters.word_matrix('F')
        COLOR = (255, 170, 0, 255)
        pyray.draw_rectangle((x * PIXEL_SIZE * 8), (y * PIXEL_SIZE * 8), PIXEL_SIZE * 8, PIXEL_SIZE * 8, COLOR_BACKGROUND_OTHER)

    elif (choice == 1):
        space_matrix = cursor
        COLOR = (255, 255, 255, 255)

    else:
        pyray.draw_rectangle((x * PIXEL_SIZE * 8), (y * PIXEL_SIZE * 8), PIXEL_SIZE * 8, PIXEL_SIZE * 8, COLOR_BACKGROUND_OTHER)
        space_matrix = bomb
        COLOR = (10, 10, 10, 255)

    for i in range(len(space_matrix)):
        for j in range(len(space_matrix[i])):
            if (space_matrix[i][j] == 1):
                pyray.draw_rectangle((x * PIXEL_SIZE * 8) + j * PIXEL_SIZE, (y * PIXEL_SIZE * 8) + i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE, COLOR)

   
def print_screen():
    # render the tartress board to the screen
    # draw background
    pyray.draw_rectangle(0, 0, WIDTH * PIXEL_SIZE, HEIGHT * PIXEL_SIZE, (70, 70, 70, 255))

    for i in range(HEIGHT // 8):
        for j in range(WIDTH // 8):
        
            # draw revealed spaces
            if (tartress.revealed[i][j] == 1):
                draw_letter(i, j, tartress.board[i][j])

            # draw flags
            if (tartress.flags[i][j] == 1):
                draw_item(i, j, 0)

            # draw cursor
            if (tartress.cursor_y == i and tartress.cursor_x == j):
                draw_item(i, j, 1)

            if (tartress.board[i][j] == 9 and show_bombs == 1):
                draw_item(i, j, 2)


# begin game
pyray.begin_drawing()

while not pyray.window_should_close() and game_loop:
    # check win state
    if (tartress.check_win()):
        game_loop = False

    # display screen
    print_screen()
   
    # if lost
    if (show_bombs == 1):
        time.sleep(3)
        game_loop = False

    before = time.time()
    # update movement limits
    if pyray.is_key_down(pyray.KEY_RIGHT):
        tartress.cursor_x += 1
         
    if pyray.is_key_down(pyray.KEY_LEFT):
        tartress.cursor_x -= 1

    if pyray.is_key_down(pyray.KEY_UP):
        tartress.cursor_y -= 1

    if pyray.is_key_down(pyray.KEY_DOWN):
        tartress.cursor_y += 1

    if pyray.is_key_down(pyray.KEY_F):
        time.sleep(0.05)
        if (tartress.flags[tartress.cursor_y][tartress.cursor_x] == 1):
            tartress.flags[tartress.cursor_y][tartress.cursor_x] = 0
            tartress.reveal(tartress.cursor_y, tartress.cursor_x)

        else:
            tartress.flags[tartress.cursor_y][tartress.cursor_x] = 1
        time.sleep(0.05)

    if pyray.is_key_down(pyray.KEY_SPACE):
        # if activate bomb
        if (tartress.board[tartress.cursor_y][tartress.cursor_x] == 9):
            show_bombs = 1
            print_screen()

        elif (tartress.count_flags(tartress.cursor_y, tartress.cursor_x) == tartress.board[tartress.cursor_y][tartress.cursor_x]):
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

    after = time.time()
    
    time.sleep(abs(0.075 - (after - before)))

    pyray.end_drawing()


pyray.close_window()
