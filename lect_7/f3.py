
class Complex:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        res = (self.x**2 + self.y**2)**0.5
        return res

    def __bool__(self):
        return not(self.x == 0 and self.y == 0)

        # if self.x == 0 and self.y == 0:
        #     return False
        # else:
        #     return True
    def __str__(self):
        return f'Complex: {self.x} + {self.y}i'

    def __int__(self):
        return int(self.x)


    def __float__(self):
        return float(self.x)

    def __complex__(self):
        return complex(self.x, self.y)

if __name__ == '__main__':
    z1 = Complex(3, 4)
    print(abs(z1))
    print(bool(z1))
    print(z1)
    print(int(z1))
    print(float(z1))
    print(complex(z1))