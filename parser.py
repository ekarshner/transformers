from display import *
from matrix import *
from draw import *

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
    f = open(fname, 'r')
    book = f.read()
    f.close()

    linelist = book.split('\n')
    i = 0
    while i < len(linelist):
        if(linelist[i] == "line"):
            temp = linelist[i+1].split()
            add_edge(points, int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3]), int(temp[4]), int(temp[5]))
            i += 1

        elif(linelist[i] == "ident"):
            ident(transform)

        elif(linelist[i] == "scale"):
            myarray = linelist[i+1].split()
            temp = make_scale(int(myarray[0]), int(myarray[1]), int(myarray[2]))
            matrix_mult(temp, transform)
            i += 1

        elif(linelist[i] == "move"):
            myarray = linelist[i+1].split()
            temp = make_translate(int(myarray[0]), int(myarray[1]), int(myarray[2]))
            matrix_mult(temp, transform)
            i += 1

        elif(linelist[i] == "rotate"):
            myarray = linelist[i+1].split()
            if myarray[0] == "x":
                temp = make_rotX(int(myarray[1]))
            elif myarray[0] == "y":
                temp = make_rotY(int(myarray[1]))
            elif myarray[0] == "z":
                temp = make_rotZ(int(myarray[1]))
            matrix_mult(temp, transform)
            i += 1

        elif(linelist[i] == "apply"):
            matrix_mult(transform, points)

        elif(linelist[i] == "display"):
            clear_screen(screen)
            for rows in range(len(points)):
                for cols in range(len(points[rows])):
                    points[rows][cols] = int(points[rows][cols])
            draw_lines(points, screen, color)
            display(screen)

        elif(linelist[i] == "save"):
            nom = linelist[i+1]
            save_extension(screen, nom)
            i += 1

        elif(linelist[i] == "quit"):
            return

        else:
            print("line not recognized: ")
            print linelist[i]
        i += 1
