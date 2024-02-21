class RectangularParallelepiped:
    def __init__(self, a, b, c):
        assert a > 0 and b > 0 and c > 0
        self.a = a
        self.b = b
        self.c = c
    def perimeterOrVolume(self):
        return self.a * self.b * self.c
    def area(self):
        return 2 * self.a * self.b + 2 * self.a * self.c + 2 * self.b * self.c
    def __str__(self) -> str:
        return f"RectangularParallelepiped: a={self.a} b={self.b} c={self.c}"