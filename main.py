from Pyramid import  Pyramid

print 'Type in the two variables you already know. If you don\'t know a variable, type in "0".'

a = float(input('a = '))
h = float(input('h = '))
M = float(input('M = '))
O = float(input('O = '))
V = float(input('V = '))
hD = float(input('hD = '))
d = float(input('d = '))
G = float(input('G = '))
s = float(input('s = '))

variables = {}
if a != 0:
    variables['a'] = a
if h != 0:
    variables['h'] = h
if M != 0:
    variables['M'] = M
if O != 0:
    variables['O'] = O
if V != 0:
    variables['V'] = V
if hD != 0:
    variables['hD'] = hD
if d != 0:
    variables['d'] = d
if G != 0:
    variables['G'] = G
if s != 0:
    variables['s'] = s

pyramid = Pyramid(variables)

if pyramid.a != 0 and pyramid.h != 0:
    print 'a = ' + str(round(pyramid.a, 2))
    print 'h = ' + str(round(pyramid.h, 2))
    print 'hD = ' + str(round(pyramid.hD, 2))
    print 'M = ' + str(round(pyramid.M,2))
    print 'G = ' + str(round(pyramid.G, 2))
    print 'O = ' + str(round(pyramid.O, 2))
    print 'V = ' + str(round(pyramid.V, 2))
    print 'd = ' + str(round(pyramid.d, 2))
    print 's = ' + str(round(pyramid.s, 2))

else:
    print "Don't you dare. This combination of variables can not be converted into other variables or is too hard for me to program."