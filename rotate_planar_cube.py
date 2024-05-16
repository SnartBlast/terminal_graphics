
from cube import Cube
from graphics_2 import Graphics
import getpass
import time
import os

if __name__ == '__main__':
    graphics = Graphics(75, 78, '234', '214')
    cube = Cube(37, 39, 0, 18)

    check_z = True
    z = 1.5

    # define all shape faces
    while True:
        # change z coordinate
        if (check_z):
            if (z < 2.5):
                z += 0.05
            else:
                check_z = False

        else:
            if (z > - 2.5):
                z -= 0.05
            else:
                check_z = True

        # front face
        tri0 = ((cube.z_verts[0] + cube.z_verts[1] + cube.z_verts[2] + cube.z_verts[3]) / 4,
                  cube.x_verts[0], cube.y_verts[0], cube.z_verts[0],
                  cube.x_verts[1], cube.y_verts[1], cube.z_verts[1],
                  cube.x_verts[2], cube.y_verts[2], cube.z_verts[2],
                  '34')
        tri1 = ((cube.z_verts[0] + cube.z_verts[2] + cube.z_verts[3] + cube.z_verts[1]) / 4,
                  cube.x_verts[0], cube.y_verts[0], cube.z_verts[0],
                  cube.x_verts[2], cube.y_verts[2], cube.z_verts[2],
                  cube.x_verts[3], cube.y_verts[3], cube.z_verts[3],
                  '34')

        # back face
        tri2 = ((cube.z_verts[4] + cube.z_verts[5] + cube.z_verts[6] + cube.z_verts[7]) / 4,
                  cube.x_verts[4], cube.y_verts[4], cube.z_verts[4],
                  cube.x_verts[5], cube.y_verts[5], cube.z_verts[5],
                  cube.x_verts[7], cube.y_verts[7], cube.z_verts[7],
                  '51')
        tri3 = ((cube.z_verts[4] + cube.z_verts[5] + cube.z_verts[6] + cube.z_verts[7]) / 4,
                  cube.x_verts[5], cube.y_verts[5], cube.z_verts[5],
                  cube.x_verts[6], cube.y_verts[6], cube.z_verts[6],
                  cube.x_verts[7], cube.y_verts[7], cube.z_verts[7],
                  '51')

        # right face
        tri4 = ((cube.z_verts[1] + cube.z_verts[2] + cube.z_verts[5] + cube.z_verts[6]) / 4,
                  cube.x_verts[1], cube.y_verts[1], cube.z_verts[1],
                  cube.x_verts[2], cube.y_verts[2], cube.z_verts[2],
                  cube.x_verts[6], cube.y_verts[6], cube.z_verts[6],
                  '15')
        tri5 = ((cube.z_verts[1] + cube.z_verts[2] + cube.z_verts[5] + cube.z_verts[6]) / 4,
                  cube.x_verts[1], cube.y_verts[1], cube.z_verts[1],
                  cube.x_verts[5], cube.y_verts[5], cube.z_verts[5],
                  cube.x_verts[6], cube.y_verts[6], cube.z_verts[6],
                  '15')

        # left face
        tri6 = ((cube.z_verts[0] + cube.z_verts[3] + cube.z_verts[4] + cube.z_verts[7]) / 4,
                  cube.x_verts[0], cube.y_verts[0], cube.z_verts[0],
                  cube.x_verts[3], cube.y_verts[3], cube.z_verts[3],
                  cube.x_verts[4], cube.y_verts[4], cube.z_verts[4],
                  '220')
        tri7 = ((cube.z_verts[0] + cube.z_verts[3] + cube.z_verts[4] + cube.z_verts[7]) / 4,
                  cube.x_verts[3], cube.y_verts[3], cube.z_verts[3],
                  cube.x_verts[4], cube.y_verts[4], cube.z_verts[4],
                  cube.x_verts[7], cube.y_verts[7], cube.z_verts[7],
                  '220')

        # bottom face
        tri8 = ((cube.z_verts[0] + cube.z_verts[1] + cube.z_verts[4] + cube.z_verts[5]) / 4,
                  cube.x_verts[0], cube.y_verts[0], cube.z_verts[0],
                  cube.x_verts[1], cube.y_verts[1], cube.z_verts[1],
                  cube.x_verts[5], cube.y_verts[5], cube.z_verts[5],
                  '213')
        tri9 = ((cube.z_verts[0] + cube.z_verts[1] + cube.z_verts[4] + cube.z_verts[5]) / 4,
                  cube.x_verts[0], cube.y_verts[0], cube.z_verts[0],
                  cube.x_verts[4], cube.y_verts[4], cube.z_verts[4],
                  cube.x_verts[5], cube.y_verts[5], cube.z_verts[5],
                  '213')

        # top face
        tri10 = ((cube.z_verts[2] + cube.z_verts[3] + cube.z_verts[6] + cube.z_verts[7]) / 4,
                  cube.x_verts[2], cube.y_verts[2], cube.z_verts[2],
                  cube.x_verts[3], cube.y_verts[3], cube.z_verts[3],
                  cube.x_verts[6], cube.y_verts[6], cube.z_verts[6],
                  '33')
        tri11 = ((cube.z_verts[2] + cube.z_verts[3] + cube.z_verts[6] + cube.z_verts[7]) / 4,
                  cube.x_verts[3], cube.y_verts[3], cube.z_verts[3],
                  cube.x_verts[6], cube.y_verts[6], cube.z_verts[6],
                  cube.x_verts[7], cube.y_verts[7], cube.z_verts[7],
                  '33')

        # front face lines
        line0 = ((cube.z_verts[0] + cube.z_verts[1]) - 20.0, 
                  cube.x_verts[0], cube.y_verts[0], cube.z_verts[0],
                  cube.x_verts[1], cube.y_verts[1], cube.z_verts[1],
                  '240')
        line1 = ((cube.z_verts[0] + cube.z_verts[3]) - 20.0, 
                  cube.x_verts[0], cube.y_verts[0], cube.z_verts[0],
                  cube.x_verts[3], cube.y_verts[3], cube.z_verts[3],
                  '240')
        line2 = ((cube.z_verts[1] + cube.z_verts[2]) - 20.0, 
                  cube.x_verts[1], cube.y_verts[1], cube.z_verts[1],
                  cube.x_verts[2], cube.y_verts[2], cube.z_verts[2],
                  '240')
        line3 = ((cube.z_verts[2] + cube.z_verts[3]) - 20.0, 
                  cube.x_verts[2], cube.y_verts[2], cube.z_verts[2],
                  cube.x_verts[3], cube.y_verts[3], cube.z_verts[3],
                  '240')

        # connecting lines
        line4 = ((cube.z_verts[0] + cube.z_verts[4]) - 20.0, 
                  cube.x_verts[0], cube.y_verts[0], cube.z_verts[0],
                  cube.x_verts[4], cube.y_verts[4], cube.z_verts[4],
                  '240')
        line5 = ((cube.z_verts[1] + cube.z_verts[5]) - 20.0, 
                  cube.x_verts[1], cube.y_verts[1], cube.z_verts[1],
                  cube.x_verts[5], cube.y_verts[5], cube.z_verts[5],
                  '240')
        line6 = ((cube.z_verts[2] + cube.z_verts[6]) - 20.0, 
                  cube.x_verts[2], cube.y_verts[2], cube.z_verts[2],
                  cube.x_verts[6], cube.y_verts[6], cube.z_verts[6],
                  '240')
        line7 = ((cube.z_verts[3] + cube.z_verts[7]) - 20.0, 
                  cube.x_verts[3], cube.y_verts[3], cube.z_verts[3],
                  cube.x_verts[7], cube.y_verts[7], cube.z_verts[7],
                  '240')

        # back face lines
        line8 = ((cube.z_verts[4] + cube.z_verts[5]) - 20.0, 
                  cube.x_verts[4], cube.y_verts[4], cube.z_verts[4],
                  cube.x_verts[5], cube.y_verts[5], cube.z_verts[5],
                  '240')
        line9 = ((cube.z_verts[4] + cube.z_verts[7]) - 20.0, 
                  cube.x_verts[4], cube.y_verts[4], cube.z_verts[4],
                  cube.x_verts[7], cube.y_verts[7], cube.z_verts[7],
                  '240')
        line10 = ((cube.z_verts[5] + cube.z_verts[6]) - 20.0, 
                  cube.x_verts[5], cube.y_verts[5], cube.z_verts[5],
                  cube.x_verts[6], cube.y_verts[6], cube.z_verts[6],
                  '240')
        line11 = ((cube.z_verts[6] + cube.z_verts[7]) - 20.0, 
                  cube.x_verts[6], cube.y_verts[6], cube.z_verts[6],
                  cube.x_verts[7], cube.y_verts[7], cube.z_verts[7],
                  '240')

        # add polygons to buffer
        graphics.add_buffer_item(tri0)
        graphics.add_buffer_item(tri1)
        graphics.add_buffer_item(tri2)
        graphics.add_buffer_item(tri3)
        graphics.add_buffer_item(tri4)
        graphics.add_buffer_item(tri5)
        graphics.add_buffer_item(tri6)
        graphics.add_buffer_item(tri7)
        graphics.add_buffer_item(tri8)
        graphics.add_buffer_item(tri9)
        graphics.add_buffer_item(tri10)
        graphics.add_buffer_item(tri11)
       
        
        # add lines to buffer 
        graphics.add_buffer_item(line0)
        graphics.add_buffer_item(line1)
        graphics.add_buffer_item(line2)
        graphics.add_buffer_item(line3)
        graphics.add_buffer_item(line4)
        graphics.add_buffer_item(line5)
        graphics.add_buffer_item(line6)
        graphics.add_buffer_item(line7)
        graphics.add_buffer_item(line8)
        graphics.add_buffer_item(line9)
        graphics.add_buffer_item(line10)
        graphics.add_buffer_item(line11)
        

        # update cube
        cube.rotate_x(2)
        cube.rotate_y(1)
        cube.rotate_z(z)
         
        # render graphics
        graphics.print()
        graphics.clear()
        time.sleep(0.09)
