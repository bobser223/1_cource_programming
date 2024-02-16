import math
class cone:
    def __init__(self, r, h):
        self.r=r
        self.h=h
    def volume(self, r, h):
        l = ((self.r ** 2 + self.h ** 2) ** 0.5)
        return math.pi*self.r*(self.r+l)
    def square(self):
        l=((self.r**2+self.h**2)**0.5)
        return ((math.pi*self.r*(self.r+l))+(math.pi*self.r**2))
