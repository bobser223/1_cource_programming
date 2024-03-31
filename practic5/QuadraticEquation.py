from Equation import Equation

class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        super().__init__(b, c)
        self._a = a
    def __str__(self):
        # return f'{self._a}x**2 + ' + super().__str__()

        return f'{self._a}x**2 + {super().__str__()}'

    def discr(self):
        return self._b ** 2 - 4 * self._a * self._c

    def solve(self):

        if self._a == 0:
            return super().solve()
        else:
            d = self.discr()
            if d < 0:
                return ()
            if d == 0:
                x1 = -self._b / (2 * self._a)
                return (x1, )
            else: # d > 0
                d_sqrt = d ** 0.5
                x1 = (-self._b + d_sqrt) / (2 * self._a)
                x2 = (-self._b - d_sqrt) / (2 * self._a)
                return (x1, x2)




if __name__ == "__main__":
    e = QuadraticEquation(1, 2, 3)
    print(e)
    e =  QuadraticEquation(0, 5, 4)
    # print(e)
    print(e.solve())
    e =  QuadraticEquation(0, 0, 4)
    print(e.solve())
    e =  QuadraticEquation(0, 0, 0)
    print(e.solve())
    e =  QuadraticEquation(0, 5, 0)
    print(e.solve())
    e = QuadraticEquation(1, 3, 8)
    # print(e)
    print(e.solve())
    e = QuadraticEquation(1, 4, 4)
    # print(e)
    print(e.solve())
    e = QuadraticEquation(1, -3, 2)
    # print(e)
    print(e.solve())

    e = QuadraticEquation(2, -6, 4)
    # print(e)
    print(e.solve())

