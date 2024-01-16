from cube import Cube
from graphics import Graphics
import time
import os

if __name__ == '__main__':
    graphics = Graphics(0.95)
    cube = Cube(25, 25, 0, 10)



    while True:
        
        # draw cube front
        graphics.draw_line(cube.x_verts[0], cube.y_verts[0], cube.x_verts[1], cube.y_verts[1])
        graphics.draw_line(cube.x_verts[1], cube.y_verts[1], cube.x_verts[2], cube.y_verts[2])
        graphics.draw_line(cube.x_verts[2], cube.y_verts[2], cube.x_verts[3], cube.y_verts[3])
        graphics.draw_line(cube.x_verts[3], cube.y_verts[3], cube.x_verts[0], cube.y_verts[0])
        

        # draw cube back
        graphics.draw_line(cube.x_verts[4], cube.y_verts[4], cube.x_verts[5], cube.y_verts[5])
        graphics.draw_line(cube.x_verts[5], cube.y_verts[5], cube.x_verts[6], cube.y_verts[6])
        graphics.draw_line(cube.x_verts[6], cube.y_verts[6], cube.x_verts[7], cube.y_verts[7])
        graphics.draw_line(cube.x_verts[7], cube.y_verts[7], cube.x_verts[4], cube.y_verts[4])

        
        # draw cube connections
        graphics.draw_line(cube.x_verts[0], cube.y_verts[0], cube.x_verts[4], cube.y_verts[4])
        graphics.draw_line(cube.x_verts[1], cube.y_verts[1], cube.x_verts[5], cube.y_verts[5])
        graphics.draw_line(cube.x_verts[2], cube.y_verts[2], cube.x_verts[6], cube.y_verts[6])
        graphics.draw_line(cube.x_verts[3], cube.y_verts[3], cube.x_verts[7], cube.y_verts[7])


        cube.rotate_y(5)  
        cube.rotate_x(1)  
        cube.rotate_z(1)  
        cube.report()
        graphics.print_board()
        graphics.clear_board()
        # 10.0 Hz refresh rate
        time.sleep(0.1)





