class rectangle:
    def __init__(self, height, width):
        self.H = height
        self.W = width
    def print(self):
        for row in range(self.H):
            print("#"*self.W)
    def widen(self,factor):
        self.W *= factor
    