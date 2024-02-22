from math import pi

class Circle:
    def __init__(self, r):
        assert r > 0
        self.r = r
        self.roundedPi = round(pi, 5)
    def length(self):
        result = 2 * self.roundedPi * self.r
        return result
    def area(self):
        result = self.roundedPi * self.r ** 2

        return result
    def __str__(self) -> str:
        return f"Circle: r={self.r}"