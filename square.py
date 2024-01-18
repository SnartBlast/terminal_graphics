import math

class Square():
    def __init__(self, x=25, y=25, z=0, chord=7):
        self.x = x
        self.y = y
        self.z = z
        self.x_verts = [x + chord, x + chord, x - chord, x - chord]
        self.y_verts = [y + chord, y - chord, y - chord, y + chord]
        self.z_verts = [z, z, z, z]
        self.magnitude = math.sqrt(pow(chord, 2) * 2)
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


    def scale(self, factor):
        # scale the size of the shape
        self.mag = self.mag * factor


    def rotate_x(self, degree):
        # rotate about the y-axis
        for i in range(4):
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
        for i in range(4):
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
            print('x ->', x, 'z ->', z)
            self.x_verts[i] = self.x + x
            self.z_verts[i] = self.z + z


        
    def rotate_z(self, degree):
        # rotate about the y-axis
        for i in range(4):
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



















        """
        # rotate abuot the z-axix
        for i in range(4):
            # get distances
            vert_x, vert_y, vert_z = self.x_verts[i], self.y_verts[i], self.z_verts[i]
            dist_x = vert_x - self.x
            dist_y = vert_y - self.y
            dist_z = vert_z - self.z
            #magnitude = math.sqrt((dist_x ** 2) + (dist_y ** 2) + (dist_z ** 2))

            # find current angle
            angle = math.degrees(math.atan2(dist_y, dist_x)) + degree
            if (angle < 0):
                angle += 360

            # apply new angle to vertices
            new_x = self.x + (math.cos(math.radians(angle)) * self.magnitude)
            new_y = self.y + (math.sin(math.radians(angle)) * self.magnitude)
            self.x_verts[i] = new_x
            self.y_verts[i] = new_y



    """
    def rotate_z1(self, degree):
        # second attempt at rotate
        magnitude = self.mag

        for i in range(4):
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

            if (new_x == vert_x or new_y == vert_y):
                self.angle += angle

            self.x_verts[i] = new_x
            self.y_verts[i] = new_y



