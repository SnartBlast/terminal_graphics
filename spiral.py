from graphics import Graphics
import sys
import time
import math

graphics = Graphics()
startX, startY = 24, 27
endX, endY = 0, 0
magnitude = 2
degree = 0
increment = 0

while (True):
    endX = startX + math.cos(math.radians(degree)) * round(magnitude)
    endY = startY + math.sin(math.radians(degree)) * round(magnitude)

    graphics.draw_line(startX, startY, endX, endY, '[48;5;15m')

    degree += 5
    magnitude += 0.05


    graphics.print_board(0)
    time.sleep(0.09)



