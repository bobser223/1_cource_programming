class I:
    def __init__(self, a):
        assert type(a) == int
        self.a = a

    def __add__(self, other):
        if type(other) == I:
            return I(self.a + other.a)
        else:
            raise TypeError('tttt')


    def __mul__(self, other):
        assert type(other) != float
        if type(other) == int:
            return I(self.a * I)

        elif type(other) == I:
            return I(self.a * other.a)




    def __str__(self):
        return str(self.a)

class R(I):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def __add__(self, other):

        if type(other) == I:
            new_a = self.a + other.a * self.b
            return R(new_a, self.b)

        elif type(other) == R:
            new_a = self.a * other.b + self.b * other.a
            new_b = self.b * other.b
            return R(new_a, new_b)

    def __mul__(self, other):
        if type(other) == int:
            new_a = self.a * other
            return R(new_a, self.b)
        elif type(other) == I:
            new_a = self.a * other.a
            return R(new_a, self.b)
        elif type(other) == R:
            new_a = self.a * other.a
            new_b = self.b * other.b
            return R(new_a, new_b)
        
    def __str__(self):
        return f'R {self.a} / {self.b}'

print( R(1, 2) * 66 + I(7) + R(3, 4) )
print(I(6) + I(8) + I(9))
r = R(2, 3)
i = I(7)



