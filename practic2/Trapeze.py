
class Trapeze:
    def __init__(self, a, b, c, d):
        assert a > 0 & b > 0 & c > 0 & d > 0 & a + b > c & a + b > d
        # основи
        self.a = a
        self.b = b
        # бічні
        self.c = c
        self.d = d
    def perimeter(self):
        result = self.a + self.b + self.c + self.d
        return result
    def square(self):
        result = ((self.a + self.b) / 2) * (self.c ** 2 - (((self.a - self.b)**2 + self.c ** 2 - self.d ** 2)/(2 * (self.a - self.b)))**2) ** 0.5
        return result