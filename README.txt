*   01-04-2023
*   Created by Kian Arnold


INTRODUCTION
====================

Hello and welcome to Kiwi's terminal graphics module!

The goal of this collection of programs is to effectively and cleanly draw shapes to the 
gitbash terminal in real time. I made this module in order to avoid having to use any 
additional programs to create graphics with Python3. 

If you're looking for a way to draw to the screen without using outside graphics programs,
then this module is for you! This git repo indcludes a couple of files. 

   *   graphics.py
      - this file handles drawing lines and pixels to a board. This class
	requires 2 parameters: width and height of your screen. The 
	default arguements for this are the width and height of my 
	screen. Larger values for width and height allow for more pixels
	and therefore a greater resolution

			.draw_line() -> given starting and ending coordinates, this method draws 
					on the 'board' attribute
			.print_board() -> this method prints the board to the terminal
			.clear_board() -> this method clears the board 

		square.py -> this file defines the vertices for a square that can be used within 
				the graphics class. 

			.translate_x() -> given a distance, translate all vertices that distance
						on the x axis
			.translate_y() -> given a distance, translate all vertices that distance
						on the y axis
			.rotate() -> given a degree, rotate all vertices about the origin 

		clock.py -> this file is a driver for a clock animation

		rotate_square.py -> this file is a drive for a rotating square animation

