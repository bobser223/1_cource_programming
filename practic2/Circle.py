from math import pi

class Circle:
    def __init__(self, r):
        assert r > 0
        self.r = r
    def perimeter(self): #LENTH
        result = 2 * pi * self.r
        return result
    def length(self):
        result = 2 * pi * self.r
        return result
    def area(self):
        result = pi * self.r ** 2
        return result
    def __str__(self) -> str:
        return f"Circle: r={self.r}"