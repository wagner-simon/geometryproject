from Pyramid import Pyramid
class Body:
    def __init__(self):
        print 'Type in the two variables you already know. If you don\'t know a variable, type in "0".'
        self.a = float(raw_input('a = '))
        self.h = float(raw_input('h = '))
        self.M = float(raw_input('M = '))
        self.O = float(raw_input('O = '))
        self.V = float(raw_input('V = '))
        self.hD = float(raw_input('hD = '))
        self.d = float(raw_input('d = '))
        self.G = float(raw_input('G = '))
        self.s = float(raw_input('s = '))

    def pyramid(self):
        variables = {}
        if self.a != 0:
            variables['a'] = self.a
        if self.h != 0:
            variables['h'] = self.h
        if self.M != 0:
            variables['M'] = self.M
        if self.O != 0:
            variables['O'] = self.O
        if self.V != 0:
            variables['V'] = self.V
        if self.hD != 0:
            variables['hD'] = self.hD
        if self.d != 0:
            variables['d'] = self.d
        if self.G != 0:
            variables['G'] = self.G
        if self.s != 0:
            variables['s'] = self.s

        return Pyramid(variables)
