from R import R



class I(int):
    def __add__(self, other):
        if type(other) == int or type(other) == I:
            return I(super().__add__(other))
        elif type(other) == I:
            return I(super().__add__(other.num))
        elif type(other) == R:
            new_a = other._a + super().__mul__(other._b)
            return R(new_a, other._b)
        else:
            raise TypeError('addition doestn supported between this two classes')

    def __mul__(self, other):
        if type(other) == I:
            return I(super().__mul__(other.num))
        elif type(other) == int or type(other) == I:
            return I(super().__mul__(other))
        elif type(other) == R:
            return R(super().__mul__(other._a), other._b)

print(I(7) + 3)
print(I(7) + I(7) + 3)
print(I(7) + R(4, 5))
print(I(7) * 5)
print(I(5) * R(5, 5))