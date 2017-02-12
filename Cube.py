from Square import Square

class Cube():
    def __init__(self, args):
        for key, value in args.iteritems():
            setattr(self, key, value)
        self.calculateA()
        variables = {}
        variables['a'] = self.a
        self.square = Square(variables)
        self.calculateV()
        self.calculateO()

    def calculateA(self):
        if hasattr(self, 'V'):
            self.a = self.V ** 1 / 3
        if hasattr(self, 'O'):
            self.a = self.O / 6 ** .5

    def calculateV(self):
        self.V = self.a ** 3

    def calculateO(self):
        self.O = self.square.O * 6