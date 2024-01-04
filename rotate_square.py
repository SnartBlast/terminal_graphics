from square import Square
from graphics import Graphics
import time

if __name__ == '__main__':
    square = Square(25, 25, 13)
    graphics = Graphics()

    while True:
        for i in range(-1, 3):
            graphics.draw_line(square.x_verts[i], square.y_verts[i], square.x_verts[i + 1], square.y_verts[i + 1], 0)

            
            #graphics.draw_point_pixel(square.x_verts[i], square.y_verts[i])
        
        graphics.draw_point_pixel(square.x, square.y)
        

        square.rotate(4)        
        graphics.print_board()
        print(graphics.angle)
        time.sleep(0.1)
        graphics.clear_board()






