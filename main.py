from Body import  Body
bodyInput = raw_input('Type in the type of geometric object you want to know stuff about(pyramid) ')
'''
print 'Type in the two variables you already know. If you don\'t know a variable, type in "0".'
a = float(raw_input('a = '))
h = float(raw_input('h = '))
M = float(raw_input('M = '))
O = float(raw_input('O = '))
V = float(raw_input('V = '))
hD = float(raw_input('hD = '))
d = float(raw_input('d = '))
G = float(raw_input('G = '))
s = float(raw_input('s = '))
'''
body = Body()
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