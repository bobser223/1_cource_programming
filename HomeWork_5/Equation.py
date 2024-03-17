class Equation:
    INF = "Infinity"
    def __init__(self, b, c):
        self._b = b
        self._c = c

    def __str__(self):
        return f'{self._b}x + {self._c} = 0'

    def show(self):
        # print(f'{self._b}x + {self._c} = 0')
        print(self)

    INF = "Infinity"

    def solve(self):
        if self._b == 0:
            if self._c == 0:
                return Equation.INF
            else: # c != 0
                return ()
        else: # b != 0
            return (-self._c / self._b, )



if __name__ == '__main__':
    e = Equation(5, 4)
    print(e)
    print(e.solve())
    e = Equation(0, 4)
    print(e.solve())
    e = Equation(0, 0)
    print(e.solve())
    e = Equation(5, 0)
    print(e.solve())
    