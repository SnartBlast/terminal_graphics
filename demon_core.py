from square import Square
from graphics import Graphics
import time
import os

if __name__ == '__main__':
    square = Square(25, 25, 13)
    square1 = Square(25, 25, 13)
    graphics = Graphics()
    count = 5

    while True:
        graphics.draw_line(square.x_verts[0], square.y_verts[0], square.x_verts[1], square.y_verts[1], 1)
        graphics.draw_line(square.x_verts[0], square.y_verts[0], square.x_verts[2], square.y_verts[2], 1)
        graphics.draw_line(square.x_verts[2], square.y_verts[2], square.x_verts[3], square.y_verts[3], 1)
        graphics.draw_line(square.x_verts[3], square.y_verts[3], square.x_verts[1], square.y_verts[1], 1)
        graphics.draw_line(square1.x_verts[0], square1.y_verts[0], square1.x_verts[1], square1.y_verts[1], 1)
        graphics.draw_line(square1.x_verts[0], square1.y_verts[0], square1.x_verts[2], square1.y_verts[2], 1)
        graphics.draw_line(square1.x_verts[2], square1.y_verts[2], square1.x_verts[3], square1.y_verts[3], 1)
        graphics.draw_line(square1.x_verts[3], square1.y_verts[3], square1.x_verts[1], square1.y_verts[1], 1)


        graphics.draw_point_pixel(square.x, square.y)

        square.rotate(1)        
        square1.rotate(-1)
        os.system('clear')
        graphics.print_board()
        # 13.3 
        time.sleep(0.075)



