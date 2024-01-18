
import math

class Cube():
    def __init__(self, x=25, y=25, z=0, c=4):
        # define shape origin coordinates
        self.x = x
        self.y = y
        self.z = z
        # I think this is where my stuff is going wrong

        # define all x coordinates
        self.x_verts = [x-c, x+c, x+c, x-c,
                        x-c, x+c, x+c, x-c]

        # define all y coordinates
        self.y_verts = [y+c, y+c, y-c, y-c,
                        y+c, y+c, y-c, y-c]

        # define all z coordinates
        self.z_verts = [z-c, z-c, z-c, z-c, 
                        z+c, z+c, z+c, z+c]

        self.magnitude = math.sqrt(c * 3)

        self.angle = 0





    def report(self):
        # print vertices
        print('X -> [', end='')
        for i in range(len(self.x_verts)):
            print(round(float(self.x_verts[i]), 1), end=', ')
        print(' ]')

        print('Y -> [', end='')
        for i in range(len(self.y_verts)):
            print(round(float(self.y_verts[i]), 1), end=', ')
        print(' ]')

        print('Z -> [', end='')
        for i in range(len(self.z_verts)):
            print(round(float(self.z_verts[i]), 1), end=', ')
        print(' ]')


    def translate_x(self, distance):
        self.x += distance
        for i in range(len(self.x_verts)):
            self.x_verts[i] = self.x_verts[i] + distance


    def translate_y(self, distance):
        self.y += distance
        for i in range(len(self.y_verts)):
            self.y_verts[i] = self.y_verts[i] + distance


    def translate_z(self, distance):
        self.z += distance
        for i in range(len(self.z_verts)):
            self.z_verts[i] = self.z_verts[i] + distance




    def rotate_x(self, degree):
        # rotate about the y-axis
        for i in range(8):
            # a --> sin
            # b --> cos
            # c^2 = a^2 + b^2
            a = self.y_verts[i] - self.y 
            b = self.z_verts[i] - self.z
            c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
            angle = math.degrees(math.atan2(b, a))

            # apply new angle
            y = round(math.cos(math.radians(angle + degree)), 5) * c
            z = round(math.sin(math.radians(angle + degree)), 5) * c
            self.y_verts[i] = self.y + y
            self.z_verts[i] = self.z + z



    def rotate_y(self, degree):
        # rotate about the y-axis
        for i in range(8):
            # a --> sin
            # b --> cos
            # c^2 = a^2 + b^2
            a = self.z_verts[i] - self.z 
            b = self.x_verts[i] - self.x
            c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
            angle = math.degrees(math.atan2(a, b))

            # apply new angle
            x = round(math.cos(math.radians(angle + degree)), 5) * c
            z = round(math.sin(math.radians(angle + degree)), 5) * c
            self.x_verts[i] = self.x + x
            self.z_verts[i] = self.z + z


        
    def rotate_z(self, degree):
        # rotate about the y-axis
        for i in range(8):
            # a --> sin
            # b --> cos
            # c^2 = a^2 + b^2
            a = self.y_verts[i] - self.y 
            b = self.x_verts[i] - self.x
            c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
            angle = math.degrees(math.atan2(a, b))

            # apply new angle
            x = round(math.cos(math.radians(angle + degree)), 5) * c
            y = round(math.sin(math.radians(angle + degree)), 5) * c
            self.x_verts[i] = self.x + x
            self.y_verts[i] = self.y + y









