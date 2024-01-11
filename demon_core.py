from square import Square
from graphics import Graphics
import time
import os

if __name__ == '__main__':
    square = Square(25, 25, 13)
    square1 = Square(25, 25, 13)
    square2 = Square(25, 25, 5)
    square3 = Square(25, 25, 8)
    graphics = Graphics()

    degree = 0
    check = True

    while True:
        # square 0
        graphics.draw_line(square.x_verts[0], square.y_verts[0], square.x_verts[1], square.y_verts[1], 1)
        graphics.draw_line(square.x_verts[0], square.y_verts[0], square.x_verts[2], square.y_verts[2], 1)
        graphics.draw_line(square.x_verts[2], square.y_verts[2], square.x_verts[3], square.y_verts[3], 1)
        graphics.draw_line(square.x_verts[3], square.y_verts[3], square.x_verts[1], square.y_verts[1], 1)

        # square 1 
        graphics.draw_line(square1.x_verts[0], square1.y_verts[0], square1.x_verts[1], square1.y_verts[1], 1)
        graphics.draw_line(square1.x_verts[0], square1.y_verts[0], square1.x_verts[2], square1.y_verts[2], 1)
        graphics.draw_line(square1.x_verts[2], square1.y_verts[2], square1.x_verts[3], square1.y_verts[3], 1)
        graphics.draw_line(square1.x_verts[3], square1.y_verts[3], square1.x_verts[1], square1.y_verts[1], 1)
        
        # square 2
        graphics.draw_line(square2.x_verts[0], square2.y_verts[0], square2.x_verts[1], square2.y_verts[1], 1)
        graphics.draw_line(square2.x_verts[0], square2.y_verts[0], square2.x_verts[2], square2.y_verts[2], 1)
        graphics.draw_line(square2.x_verts[2], square2.y_verts[2], square2.x_verts[3], square2.y_verts[3], 1)
        graphics.draw_line(square2.x_verts[3], square2.y_verts[3], square2.x_verts[1], square2.y_verts[1], 1)

        # square 3
        graphics.draw_line(square3.x_verts[0], square3.y_verts[0], square3.x_verts[1], square3.y_verts[1], 1)
        graphics.draw_line(square3.x_verts[0], square3.y_verts[0], square3.x_verts[2], square3.y_verts[2], 1)
        graphics.draw_line(square3.x_verts[2], square3.y_verts[2], square3.x_verts[3], square3.y_verts[3], 1)
        graphics.draw_line(square3.x_verts[3], square3.y_verts[3], square3.x_verts[1], square3.y_verts[1], 1)

        # center tile
        graphics.draw_point_pixel(square.x, square.y)

        square.rotate(degree / 2)
        square1.rotate(-degree / 2)
        square2.rotate(degree)
        square3.rotate(-degree)


        if (check):
            if (degree > 12):
                check = False
            else:
                degree += 0.1
        else:
            if (degree < -12):
                check = True
            else:
                degree -= 0.1





        #os.system('clear')
        graphics.print_board()
        graphics.clear_board()
        # 10.0 Hz refresh rate
        time.sleep(0.1)





