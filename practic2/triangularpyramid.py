class Triangularpyramid:
    def __init__(self, a, h):
        self.a = a #сторона
        self.h = h #висота
    def volume(self):
        return (1.3) * self.a ** 2 * self.h
    def area(self):
        rebro = ((self.a ** 2 + self.h ** 2) ** 0.5)
        pivper1 = rebro * 2 + self.a
        sq1 = ((pivper1 * (pivper1 - rebro) * (pivper1 - rebro) * (pivper1 - self.a)) ** 0.5)
        sq2 = ((self.a ** 2) * (3 ** 0.5)) / 4
        return sq1 * 3 + sq2
    def __str__(self) -> str:
        return f"Triangularpyramid: a={self.a} h={self.h}"


