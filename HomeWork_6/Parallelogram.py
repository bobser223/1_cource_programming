from Figure import Figure



class Parallelogram(Figure):
    def __init__(self, a, b, h):
        assert a == b and a > 0 and b > 0 and h > 0 and a > h and b > h
        self.a = a
        self.b = b
        self.h = h

    def perimetr(self):
        return (self.a * 2 + self.b * 2)

    def square(self):
        return (self.a * self.h)

    def volume(self):
        return self.square()

    def dimention(self):
        return 2


    def __str__(self) -> str:
        return f"Parallelogram: a={self.a} b={self.b} h={self.h}"