from R import R

class I:
    def __init__(self, num):
        assert type(num) == int
        self.num = num
    def __add__(self, other):
        if type(other) == int:
            return I(self.num + other)
        elif type(other) == I:
            return I(self.num + other.num)
        elif type(other) == R:
            new_a = other._a + self.num * other._b
            return R(new_a, other._b)
        else:
            raise TypeError('addition doestn supported between this two classes')

    def __mul__(self, other):
        if type(other) == I:
            return I(self.num * other.num)
        elif type(other) == int:
            return I(self.num * other)
        elif type(other) == R:
            return R(self.num * other._a, other._b)
    def __str__(self):
        return f"I {delf.num}"