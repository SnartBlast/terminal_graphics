import math

class Square():
    def __init__(self, x=25, y=25, chord=4):
        self.x = x
        self.y = y
        self.x_verts = [x + chord, x + chord, x - chord, x - chord]
        self.y_verts = [y + chord, y - chord, y + chord, y - chord]
        self.mag = math.sqrt(pow(chord, 2) * 2)
        self.angle = 0


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


    def rotate(self, degree):
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



