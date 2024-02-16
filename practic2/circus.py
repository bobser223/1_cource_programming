import math
class circus:
    def __init__(self, r):
        assert r > 0
        self.r=r
    def length(self):
        return (2*math.pi*self.r)
    def square(self):
        return (math.pi*(self.r**2))