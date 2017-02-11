class Rectangle():
    def __init__(self, args):
        for key, value in args.iteritems():
            setattr(self, key, value)
        self.calculateA()
        self.calculateB()
        self.calculateO()
        self.calculateU()

    def calculateA(self):
        if hasattr(self, 'b') and hasattr(self, 'O'):
            self.a = self.O / self.b
        if hasattr(self, 'b') and hasattr(self, 'U'):
            self.a = self.U / 2 - self.b

    def calculateB(self):
        if hasattr(self, 'a') and hasattr(self, 'O'):
            self.b = self.O / self.a
        if hasattr(self, 'a') and hasattr(self, 'U'):
            self.b = self.U / 2 - self.a

    def calculateO(self):
        if hasattr(self, 'a') and hasattr(self, 'b'):
            self.O = self.a * self.b

    def calculateU(self):
        if hasattr(self, 'a') and hasattr(self, 'b'):
            self.U = 2 * self.a + 2 * self.b