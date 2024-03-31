from I import I

class R:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __add__(self, other):

        if type(other) == int or type(other) == I:
            new_a = self._a + other * self._b
            return R(new_a, self._b)

        elif type(other) == R:
            new_a = self._a * other._b + self._b * other._a
            new_b = self._b * other._b
            return R(new_a, new_b)
        else:
            raise AssertionError

    def __mul__(self, other):
        if type(other) == int or type(other) == I:
            new_a = self._a * other
            return R(new_a, self._b)

        elif type(other) == R:
            new_a = self._a * other.a
            new_b = self._b * other.b
            return R(new_a, new_b)
        else:
            raise AssertionError

    def __str__(self):
        return f'R {self._a} / {self._b}'

