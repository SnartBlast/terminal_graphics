from cube import Cube
from graphics import Graphics
import time
import os


if __name__ == '__main__':
    graphics = Graphics(1.0)
    cube = Cube(25, 25, 0, 10)
    
    while True: 
        # front lines
        line0 = ((cube.z_verts[0] + cube.z_verts[1]) / 2, 
                  cube.x_verts[0], cube.y_verts[0],
                  cube.x_verts[1], cube.y_verts[1],
                  '[48;5;57m')
        line1 = ((cube.z_verts[1] + cube.z_verts[2]) / 2, 
                  cube.x_verts[1], cube.y_verts[1],
                  cube.x_verts[2], cube.y_verts[2],
                  '[48;5;57m')
        line2 = ((cube.z_verts[2] + cube.z_verts[3]) / 2, 
                  cube.x_verts[2], cube.y_verts[2],
                  cube.x_verts[3], cube.y_verts[3],
                  '[48;5;129m')
        line3 = ((cube.z_verts[3] + cube.z_verts[0]) / 2, 
                  cube.x_verts[3], cube.y_verts[3],
                  cube.x_verts[0], cube.y_verts[0],
                  '[48;5;129m')

        # back lines
        line4 = ((cube.z_verts[4] + cube.z_verts[5]) / 2, 
                  cube.x_verts[4], cube.y_verts[4],
                  cube.x_verts[5], cube.y_verts[5],
                  '[48;5;201m')
        line5 = ((cube.z_verts[5] + cube.z_verts[6]) / 2, 
                  cube.x_verts[5], cube.y_verts[5],
                  cube.x_verts[6], cube.y_verts[6],
                  '[48;5;201m')
        line6 = ((cube.z_verts[6] + cube.z_verts[7]) / 2, 
                  cube.x_verts[6], cube.y_verts[6],
                  cube.x_verts[7], cube.y_verts[7],
                  '[48;5;69m')
        line7 = ((cube.z_verts[7] + cube.z_verts[4]) / 2, 
                  cube.x_verts[7], cube.y_verts[7],
                  cube.x_verts[4], cube.y_verts[4],
                  '[48;5;69m')

        # connecting lines
        line8 = ((cube.z_verts[0] + cube.z_verts[4]) / 2, 
                  cube.x_verts[0], cube.y_verts[0],
                  cube.x_verts[4], cube.y_verts[4],
                  '[48;5;213m')
        line9 = ((cube.z_verts[1] + cube.z_verts[5]) / 2, 
                  cube.x_verts[1], cube.y_verts[1],
                  cube.x_verts[5], cube.y_verts[5],
                  '[48;5;213m')
        line10 = ((cube.z_verts[2] + cube.z_verts[6]) / 2, 
                  cube.x_verts[2], cube.y_verts[2],
                  cube.x_verts[6], cube.y_verts[6],
                  '[48;5;254m')
        line11 = ((cube.z_verts[3] + cube.z_verts[7]) / 2, 
                  cube.x_verts[3], cube.y_verts[3],
                  cube.x_verts[7], cube.y_verts[7],
                  '[48;5;201m')

        # add lines to buffer
        graphics.add_line(line0)
        graphics.add_line(line1)
        graphics.add_line(line2)
        graphics.add_line(line3)
        graphics.add_line(line4)
        graphics.add_line(line5)
        graphics.add_line(line6)
        graphics.add_line(line7)
        graphics.add_line(line8)
        graphics.add_line(line9)
        graphics.add_line(line10)
        graphics.add_line(line11)

        # perform shape and graphics functions
        cube.rotate_x(2)
        cube.rotate_y(3)
        cube.rotate_z(-1)
        graphics.print_board()
        #graphics.clear_board()
        time.sleep(0.1)
