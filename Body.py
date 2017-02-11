from Pyramid import Pyramid
from Sphere import Sphere


class Body:
    def __init__(self):
        pass

    def pyramid(self):
        print 'Type in the two variables you already know.'
        try:
            self.a = float(raw_input('a = '))
        except(ValueError):
            self.a = 0

        try:
            self.h = float(raw_input('h = '))
        except(ValueError):
            self.h = 0

        try:
            self.M = float(raw_input('M = '))
        except(ValueError):
            self.M = 0

        try:
            self.O = float(raw_input('O = '))
        except(ValueError):
            self.O = 0

        try:
            self.V = float(raw_input('V = '))
        except(ValueError):
            self.V = 0

        try:
            self.hD = float(raw_input('hD = '))
        except(ValueError):
            self.hD = 0

        try:
            self.d = float(raw_input('d = '))
        except(ValueError):
            self.d = 0

        try:
            self.G = float(raw_input('G = '))
        except(ValueError):
            self.G = 0

        try:
            self.s = float(raw_input('s = '))
        except(ValueError):
            self.s = 0

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

    def sphere(self):
        print 'Type in the variable you already know.'
        try:
            self.r = float(raw_input('r = '))
        except(ValueError):
            self.r = 0

        try:
            self.d = float(raw_input('d = '))
        except(ValueError):
            self.d = 0

        try:
            self.V = float(raw_input('V = '))
        except(ValueError):
            self.V = 0

        try:
            self.M = float(raw_input('O = '))
        except(ValueError):
            self.M = 0

        try:
            self.U = float(raw_input('U = '))
        except(ValueError):
            self.U = 0

        variables = {}
        if self.r != 0:
            variables['r'] = self.r
        if self.d != 0:
            variables['d'] = self.d
        if self.V != 0:
            variables['V'] = self.V
        if self.M != 0:
            variables['O'] = self.M
        if self.U != 0:
            variables['U'] = self.U

        return Sphere(variables)