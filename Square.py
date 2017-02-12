class Square():
    def __init__(self, args):
        for key, value in args.iteritems():
            setattr(self, key, value)
        self.calculateA()
        self.calculateO()
        self.calculateU()

    def calculateA(self):
        if hasattr(self, 'O'):
            self.a = self.O ** .5
        if hasattr(self, 'U'):
            self.a = self.U / 4

    def calculateO(self):
        self.O = self.a ** 2

    def calculateU(self):
        self.U = self.a * 4