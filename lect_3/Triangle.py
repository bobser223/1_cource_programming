class Triangle:
    def __init__(self, a, b, c):
        # my_list = [a, b, c]
        # my_list.sort()
        # a, b, c = my_list
        # assert a + b > c
        assert a + b > c and a + c > b and b + c > a
        self.__a = a
        self.__b = b
        self.__c = c

    def set_a(self, a):
        if a + self.__b > self.__c and a + self.__c > self.__b and self.__b + self.__c > a:
            self.__a = a
        else:
            print("змінна не підходить")

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c


    def set_b(self, b):
        if self.__a + b > self.__c and self.__a + self.__c > b and b + self.__c > self.__a:
            self.__b = b
        else:
            print("змінна не підходить")

    def set_c(self, c):
        if self.__a + self.__b > c and self.__a + c > self.__b and self.__b + c > self.__a:
            self.__c = c
        else:
            print("змінна не підходить")


    def semiperimeter(self):
        return self.perimeter() / 2
    def perimeter(self):
        return self.__a + self.__b + self.__c
    def area(self):
        result = (self.semiperimeter() * (self.semiperimeter() - self.__a) * (self.semiperimeter() - self.__b) * (self.semiperimeter() - self.__c)) ** 0.5
        return result
    # def __str__(self) -> str:
    #     return f"Triangle: a={self.a} b={self.b} c={self.c}"
    def show(self):
        print("Triangle", self.__a, self.__b, self.__c)

if __name__ == "__main__":
    try:
        t = Triangle(3, 4, 5)
        t.show()
        t.set_a(33)
        t.show()
        print("Area =", t.area())
    except AssertionError:
        print("triangle isn't exist")