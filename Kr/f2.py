class I:
    def __init__(self, a):
        assert type(a) == int
        self.a = a

    def __add__(self, other):
        if type(other) == I:
            return I(self.a + other.a)
        elif type(other) == int:
            return I(self.a + other)

    def __str__(self):
        return str(self.a)


class R(I):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def __add__(self, other):
        if type(other) == int:
            return R(self.a + other * self.b, self.b)

        elif type(other) == I:
            return R(self.a + other.a * self.b, self.b)

        elif type(other) == R:
            return R(self.a * other.b + other.a * self.b, self.b * other.b)

    def __str__(self):
        return f"R {self.a} / {self.b}"

print(R(1, 2) + I(1) + R(1, 2))