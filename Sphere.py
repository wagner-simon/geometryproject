from math import pi

class Sphere():
    def __init__(self, args):
        for key, value in args.iteritems():
            setattr(self, key, value)
        self.calculateR()
        self.calculateD()
        self.calculateV()
        self.calculateO()
        self.calculateU()

    def calculateR(self):
        if hasattr(self, 'd'):
            self.r = self.d / 2
        if hasattr(self, 'V'):
            self.r = (self.V / 3 / 4 * pi) ** 1 / 3
        if hasattr(self, 'O'):
            self.r = (self.O / 4 * pi) ** .5
        if hasattr(self, 'U'):
            self.r = self.U / 2 / pi

    def calculateD(self):
        self.d = self.r * 2

    def calculateV(self):
        self.V = (self.r) ** 3 * 4 / 3 * pi

    def calculateO(self):
        self.O = pi * self.d ** 2

    def calculateU(self):
        self.U = pi * self.d

