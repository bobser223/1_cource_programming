
class Complex:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        res = (self.x**2 + self.y**2)**0.5
        return res

if __name__ == '__main__':
    z1 = Complex(3, 4)
    print(abs(z1))