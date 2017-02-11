class Square():
    def __init__(self, args):
        for key, value in args.iteritems():
            setattr(self, key, value)
        self.calculateA()
        self.calculateV()
        self.calculateU()

    def calculateA(self):
        if hasattr(self, 'V'):
            self.a = self.V ** .5
        if hasattr(self, 'U'):
            self.a = self.U / 4

    def calculateV(self):
        self.V = self.a ** 2

    def calculateU(self):
        self.U = self.a * 4