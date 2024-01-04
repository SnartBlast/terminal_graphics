import math

class Square():
    def __init__(self, x=25, y=25, chord=5):
        self.x = x
        self.y = y
        self.x_verts = [x + chord, x + chord, x - chord, x - chord]
        self.y_verts = [y + chord, y - chord, y + chord, y - chord]


    def translate_x(self, distance):
        self.x += distance
        for i in range(len(self.x_verts)):
            self.x_verts[i] = self.x_verts[i] + distance


    def translate_y(self, distance):
        self.y += distance
        for i in range(len(self.y_verts)):
            self.y_verts[i] = self.y_verts[i] + distance


    def rotate(self, degree):
        # second attempt at rotate
        magnitude = math.sqrt(pow(self.x - self.x_verts[0], 2) + pow(self.y - self.y_verts[0], 2))

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
            self.x_verts[i] = round(new_x)
            self.y_verts[i] = round(new_y) 






