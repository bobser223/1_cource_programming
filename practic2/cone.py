from math import pi
# class cone:
#     def __init__(self, r, h):
#         self.r=r
#         self.h=h
#     def volume(self, r, h):
#         l = ((self.r ** 2 + self.h ** 2) ** 0.5)
#         return math.pi*self.r*(self.r+l)
#     def square(self):
#         l=((self.r**2+self.h**2)**0.5)
#         return ((math.pi*self.r*(self.r+l))+(math.pi*self.r**2))

class Cone:
    def __init__(self, r, h):
        assert r > 0 and h > 0
        self.r = r
        self.h = h
    def area(self):
        l = (self.h ** 2 + self.r ** 2) ** 0.5
        result = pi * self.r * (l + self.r)
        return result
    def volume(self):
        result = 1/3 * pi * (self.r ** 2) * self.h
    def __str__(self) -> str:
        return f"Cone: r={self.r} h={self.h}"