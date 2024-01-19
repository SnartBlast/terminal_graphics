
from square import Square
from graphics import Graphics
import time
import os
import math

if __name__ == '__main__':
    graphics = Graphics(1)
    square = Square(25, 25, 0, 10)   
    
    while True:
        # draw square
        graphics.draw_line(square.x_verts[0], square.y_verts[0], square.x_verts[1], square.y_verts[1])
        graphics.draw_line(square.x_verts[1], square.y_verts[1], square.x_verts[2], square.y_verts[2])
        graphics.draw_line(square.x_verts[2], square.y_verts[2], square.x_verts[3], square.y_verts[3])
        graphics.draw_line(square.x_verts[3], square.y_verts[3], square.x_verts[0], square.y_verts[0]) 
        square.rotate_x(3)
        square.rotate_y(5)
        square.rotate_z(7)
        graphics.print_board()
        graphics.clear_board()
        # 10.0 Hz refresh rate
        time.sleep(0.1)




