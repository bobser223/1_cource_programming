class QuadrangularPyramid:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    def area(self):
        result_re = self.a * self.b
        l1 = ((self.a / 2) ** 2 + self.h ** 2) ** 0.5
        l2 = ((self.b / 2) ** 2 + self.h ** 2) ** 0.5
        result_tr_1 = l1 * self.b / 2
        result_tr_2 = l2 * self.a / 2
        return result_re + 2 * result_tr_2 + 2 * result_tr_1
    def __str__(self) -> str:
        return f"QuadrangularPyramid: a={self.a} b={self.b} h={self.h}"