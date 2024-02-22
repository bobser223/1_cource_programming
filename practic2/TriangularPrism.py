class TriangularPrism:
    def __init__(self, a, b, c, l):
        self.a = a
        self.b = b
        self.c = c
        self.l = l

    def semiperimeter(self):
        return self.perimeter() / 2
    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        result_tr = (self.semiperimeter() * (self.semiperimeter() - self.a) * (self.semiperimeter() - self.b) * (self.semiperimeter() - self.c)) ** 0.5
        result_re = self.a * self.l + self.b * self.l + self.c * self.l
        result = result_tr * 2 + result_re
        if isinstance(result, complex):

            result_list = [round(result.real, 2), round(result.imag, 2)]
            nonComplexReslt = max(result_list)
            return nonComplexReslt
        else:

            return round(result, 2)


    def volume(self):
        result_tr = (self.semiperimeter() * (self.semiperimeter() - self.a) * (self.semiperimeter() - self.b) * (self.semiperimeter() - self.c)) ** 0.5
        return result_tr * self.l

    def __str__(self) -> str:
        return f"TriangularPrism: a={self.a} b={self.b} c={self.c} l={self.l}"