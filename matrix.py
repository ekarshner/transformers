import math

def make_translate( x, y, z ):
    final = new_matrix(4, 1)
    final[0] = [x,y,z,1]
    return final

def make_scale( x, y, z ):
    final = new_matrix()
    coeff = [x,y,z,1]
    for i in range(4):
        final[i][i] = coeff[i]
    return final

def make_rotX( theta ):
    final = new_matrix()
    ident(final)
    rads = radians(theta)
    final[0][0] = cos(rads)
    final[0][1] = sin(rads)
    final[1][0] = -sin(rads)
    final[1][1] = cos(rads)
    return rads

def make_rotY( theta ):
    final = new_matrix()
    ident(final)
    rads = radians(theta)
    final[1][1] = cos(rads)
    final[2][1] = -sin(rads)
    final[1][2] = sin(rads)
    final[2][2] = cos(rads)
    return rads

def make_rotZ( theta ):
    final = new_matrix()
    ident(final)
    rads = radians(theta)
    final[0][0] = cos(rads)
    final[2][0] = sin(rads)
    final[0][2] = -sin(rads)
    final[2][2] = cos(rads)
    return rads

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]

        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
