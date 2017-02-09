class Pyramid():
    def __init__(self, args):
        for key, value in args.iteritems():
            setattr(self, key, value)
        self.calculateA()
        self.calculateH()
        self.calculateHD()
        self.calculateM()
        self.calculateG()
        self.calculateO()
        self.calculateV()
        self.calculateD()
        self.calculateS()

    def calculateA(self):
        if hasattr(self, 'd'):
            self.a = (self.d ** 2 / 2) ** .5
        if hasattr(self, 'G'):
            self.a = self.G ** .5
        if hasattr(self, 'M') and hasattr(self, 'hD'):
            self.a = self.M / self.hD / 2
        if hasattr(self, 'h') and hasattr(self, 'hD'):
            self.a = 2 * (self.hD ** 2 - self.h ** 2) ** .5
        if hasattr(self, 'h') and hasattr(self, 's'):
            self.a = (2 * self.s ** 2 - 2 * self.h ** 2) ** .5
        if hasattr(self, 'h') and hasattr(self, 'd'):
            self.a = (self.d ** 2 / 2) ** .5
        if hasattr(self, 'h') and hasattr(self, 'V'):
            self.a = 3 * self.V / self.h ** .5
        if hasattr(self, 'hD') and hasattr(self, 's'):
            self.a = (-4 * self.hD ** 2 + 4 * self.s ** 2) ** .5
        if hasattr(self, 'hD') and hasattr(self, 'M'):
            self.a = self.M / (2 * self.hD)
        if hasattr(self, 'M') and hasattr(self, 'O'):
            self.a = (self.O - self.M) ** .5

    def calculateH(self):
        if hasattr(self, 'hD'):
            self.h = (self.hD - self.a ** 2 / 4) ** .5
        if hasattr(self, 's'):
            self.h = (self.s ** 2 - self.a ** 2 / 2) ** .5
        if hasattr(self, 'M'):
            self.h = ((self.M / 2 * self.a) ** 2 - (self.a / 2) ** 2) ** .5
        if hasattr(self, 'O'):
            self.h = ((self.O - self.a ** 2 / 2 * self.a) ** 2 - (self.a / 2) ** 2) ** .5
        if hasattr(self, 'V'):
            self.h = 3 * self.V / self.a ** 2

    def calculateHD(self):
            self.hD = (self.h ** 2 + (self.a / 2) ** 2) ** .5

    def calculateM(self):
            self.M = 2 * self.a * self.hD

    def calculateG(self):
            self.G = self.a ** 2

    def calculateO(self):
            self.O = self.M + self.G

    def calculateV(self):
            self.V = self.a ** 2 * self.h / 3

    def calculateD(self):
            self.d = (2 ** .5) * self.a

    def calculateS(self):
            self.s = (self.h ** 2 + self.a ** 2 / 2) ** .5
