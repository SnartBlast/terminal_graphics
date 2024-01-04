from graphics import Graphics
import sys
import time
import math


graphics = Graphics(60, 67)
startX, startY = 25, 26
endX, endY = 0, 0
magnitude = 23
degree = -10
haveX = []
haveY = []

while (True):
    #for i in range(len(haveX)):
    #    graphics.draw_point_pixel(haveX[i], haveY[i], graphics.angle)

    endX = round(startX + math.cos(math.radians(degree)) * magnitude)
    endY = round(startY + math.sin(math.radians(degree)) * magnitude)
    haveX.append(endX)
    haveY.append(endY)
    graphics.draw_line(startX, startY, endX, endY, 0)
    graphics.draw_point_pixel(endX, endY)

    degree += 5.5
    degree = degree % 360

    graphics.print_board()
    print(graphics.angle)
    time.sleep(0.09)
    #graphics.clear_board()



