class diamond:
    def __init__(self, layers):
        self.L = layers
    def print(self):
        for row in range(self.L):
            print('#'*self.L)
    def heighten(self, layers):
        self.L = layers