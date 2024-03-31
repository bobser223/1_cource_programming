class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


    @staticmethod
    def add(v1, v2):
        return Vector(v1.x + v2.x, v1.y + v2.y)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, int) or isinstance(other, float):
            x = self.x + other
            y = self.y
            return Vector(x, y)


if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1)
    print(v2)
    v3 = v1 + v2
    # v3 = Vector.add(v1, v2)
    print(v3)
    # v4 = v1 - v2
    # print(v4)
    print(v1 + 6)
    print(v3.__dict__)
    print(v3.__dict__.items())
    print(v3.__dict__.keys())
    print(v3.__dict__.values())
    print(Vector.__dict__)