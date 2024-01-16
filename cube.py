
import math

class Cube():
    def __init__(self, x=25, y=25, z=0, c=4):
        # define shape origin coordinates
        self.x = x
        self.y = y
        self.z = z
        # I think this is where my stuff is going wrong
        self.mag = math.sqrt(pow(c, 2) * 3)
        self.angle = 0

        # define all x coordinates
        self.x_verts = [x-c, x+c, x+c, x-c,
                        x-c, x+c, x+c, x-c]

        # define all y coordinates
        self.y_verts = [y+c, y+c, y-c, y-c,
                        y+c, y+c, y-c, y-c]

        # define all z coordinates
        self.z_verts = [z-c, z-c, z-c, z-c, 
                        z+c, z+c, z+c, z+c]


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


    def scale(self, factor):
        # scale the size of the shape
        self.mag = self.mag * factor


    def rotate_x(self, degree):
        # rotate about the y-axis
        magnitude = self.mag

        for i in range(8):
            # get distances
            vert_y, vert_z = self.y_verts[i], self.z_verts[i]
            dist_y = vert_y - self.y
            dist_z = vert_z - self.z

            # find current angle
            angle = math.degrees(math.atan2(dist_z, dist_y)) + degree
            if (angle < 0):
                angle += 360

            # apply new angle to vertices
            new_y = self.y + (math.cos(math.radians(angle)) * magnitude)
            new_z = self.z + (math.sin(math.radians(angle)) * magnitude)
            self.y_verts[i] = new_y
            self.z_verts[i] = new_z


    def rotate_y(self, degree):
        # rotate about the y-axis
        magnitude = self.mag

        for i in range(8):
            # get distances
            vert_x, vert_z = self.x_verts[i], self.z_verts[i]
            dist_x = vert_x - self.x
            dist_z = vert_z - self.z

            # find current angle
            angle = math.degrees(math.atan2(dist_z, dist_x)) + degree
            if (angle < 0):
                angle += 360
 
            # apply new angle to vertices
            new_x = self.x + (math.cos(math.radians(angle)) * magnitude)
            new_z = self.z + (math.sin(math.radians(angle)) * magnitude)
            self.x_verts[i] = new_x
            self.z_verts[i] = new_z


    def rotate_z(self, degree):
        # rotate abuot the z-axix
        magnitude = self.mag

        for i in range(8):
            # get distances
            vert_x, vert_y = self.x_verts[i], self.y_verts[i]
            dist_x = vert_x - self.x
            dist_y = vert_y - self.y

            # find current angle
            angle = math.degrees(math.atan2(dist_y, dist_x)) + degree
            if (angle < 0):
                angle += 360
 
            # apply new angle to vertices
            new_x = self.x + (math.cos(math.radians(angle)) * magnitude)
            new_y = self.y + (math.sin(math.radians(angle)) * magnitude)
            self.x_verts[i] = new_x
            self.y_verts[i] = new_y
