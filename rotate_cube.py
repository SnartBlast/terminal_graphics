from cube import Cube
from graphics import Graphics
import time
import os

if __name__ == '__main__':
    graphics = Graphics(0.95)
    cube = Cube(25, 25, 0, 10)
    #cube.rotate_x(30)


    while True:

        # draw cube front
        graphics.draw_line(cube.x_verts[0], cube.y_verts[0], cube.x_verts[1], cube.y_verts[1], '[48;5;51m')
        graphics.draw_line(cube.x_verts[1], cube.y_verts[1], cube.x_verts[2], cube.y_verts[2], '[48;5;52m')
        graphics.draw_line(cube.x_verts[2], cube.y_verts[2], cube.x_verts[3], cube.y_verts[3], '[48;5;53m')
        graphics.draw_line(cube.x_verts[3], cube.y_verts[3], cube.x_verts[0], cube.y_verts[0], '[48;5;54m')
        

        # draw cube back
        graphics.draw_line(cube.x_verts[4], cube.y_verts[4], cube.x_verts[5], cube.y_verts[5], '[48;5;55m')
        graphics.draw_line(cube.x_verts[5], cube.y_verts[5], cube.x_verts[6], cube.y_verts[6], '[48;5;56m')
        graphics.draw_line(cube.x_verts[6], cube.y_verts[6], cube.x_verts[7], cube.y_verts[7], '[48;5;57m')
        graphics.draw_line(cube.x_verts[7], cube.y_verts[7], cube.x_verts[4], cube.y_verts[4], '[48;5;58m')

        
        # draw cube connections
        graphics.draw_line(cube.x_verts[0], cube.y_verts[0], cube.x_verts[4], cube.y_verts[4], '[48;5;53m')
        graphics.draw_line(cube.x_verts[1], cube.y_verts[1], cube.x_verts[5], cube.y_verts[5], '[48;5;53m')
        graphics.draw_line(cube.x_verts[2], cube.y_verts[2], cube.x_verts[6], cube.y_verts[6], '[48;5;53m')
        graphics.draw_line(cube.x_verts[3], cube.y_verts[3], cube.x_verts[7], cube.y_verts[7], '[48;5;53m')
        """
        graphics.draw_point_pixel(cube.x_verts[0], cube.y_verts[0])
        graphics.draw_point_pixel(cube.x_verts[1], cube.y_verts[1])
        graphics.draw_point_pixel(cube.x_verts[2], cube.y_verts[2])
        graphics.draw_point_pixel(cube.x_verts[3], cube.y_verts[3])
        graphics.draw_point_pixel(cube.x_verts[4], cube.y_verts[4])
        graphics.draw_point_pixel(cube.x_verts[5], cube.y_verts[5])
        graphics.draw_point_pixel(cube.x_verts[6], cube.y_verts[6])
        graphics.draw_point_pixel(cube.x_verts[7], cube.y_verts[7])

        """

        #cube.rotate_x(2)  
        cube.rotate_x(3)
        cube.rotate_y(4)
        cube.rotate_z(2)
        graphics.print_board()
        graphics.clear_board()
        # 10.0 Hz refresh rate
        time.sleep(0.1)





