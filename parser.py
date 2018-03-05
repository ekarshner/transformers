from display import *
from matrix import *
from draw import *
import re

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix -
	 scale: create a scale matrix,
	    then multiply the transform matrix by the scale matrix -
	    takes 3 arguments (sx, sy, sz)
    ident
	 move: create a translation matrix,
	    then multiply the transform matrix by the translation matrix -
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    with open(fname) as fp:
        for line in enumerate(fp):
            if(line == "line"):
                line = fp.readline()
                temp = line.split()
                add_edge(points, temp[0], temp[1], temp[2], temp[3], temp[4], temp[5])

            elif(line == "ident"):
                ident(transform)

            elif(line == "scale"):
                line = fp.readline()
                myarray = line.split()
                temp = make_scale(myarray[0], myarray[1], myarray[2])
                transform = matrix_mult(transform, temp)

            elif(line == "move"):
                line = fp.readline()
                myarray = line.split()
                temp = make_translate(myarray[0], myarray[1], myarray[2])
                transform = matrix_mult(transform, temp)

            elif(line == "rotate"):
                line = fp.readline()
                myarray = line.split()
                if myarray[0] = "x":
                    temp = make_rotX(myarray[1])
                    transform = matrix_mult(transform, temp)
                elif myarray[0] = "y":
                    temp = make_rotX(myarray[1])
                    transform = matrix_mult(transform, temp)
                elif myarray[0] = "z":
                    temp = make_rotX(myarray[1])
                    transform = matrix_mult(transform, temp)

            elif(line == "apply"):
                points = matrix_mult(transform, points)

            elif(line == "display"):
                draw_lines(points, screen, color)
                display(screen)

            elif(line == "save"):
                save_extension(screen, 'img.png')

            elif(line == "quit"):
                return

            else:
                print("line not recognized: ")
                print line
