from Body import  Body
print 'This program will calculate the values of geometric objects for you'
print '1: Pyramid'
print '2: Sphere'
print 'choose a object by typing in it\'s number'
bodyInput = raw_input()

body = Body()
if bodyInput == '1':
    pyramid = body.pyramid()
    if pyramid.a != 0 and pyramid.h != 0:
        print ''
        print 'a = ' + str(round(pyramid.a, 2))
        print 'h = ' + str(round(pyramid.h, 2))
        print 'hD = ' + str(round(pyramid.hD, 2))
        print 'M = ' + str(round(pyramid.M, 2))
        print 'G = ' + str(round(pyramid.G, 2))
        print 'O = ' + str(round(pyramid.O, 2))
        print 'V = ' + str(round(pyramid.V, 2))
        print 'd = ' + str(round(pyramid.d, 2))
        print 's = ' + str(round(pyramid.s, 2))
    else:
        print ''
        print "Don't you dare. This combination of variables can not be converted into other variables or is too hard for me to program."

if bodyInput == '2':
    sphere = body.sphere()
    print ''
    print 'r = ' + str(round(sphere.r, 2))
    print 'd = ' + str(round(sphere.d, 2))
    print 'V = ' + str(round(sphere.V, 2))
    print 'O = ' + str(round(sphere.O, 2))
    print 'U = ' + str(round(sphere.U, 2))