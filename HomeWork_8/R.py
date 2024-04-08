
class R:
    def __init__(self, a, b=1):
        if isinstance(a, int) and isinstance(b, int):
            self._a = a
            self._b = b
        if isinstance(a, str):
            if "/" in a:
                for j in range(len(a)):
                    if a[j] == "/":
                        try:
                            self._a = int(a[0: j])
                            self._b = int(a[j + 1:])
                        except ValueError:
                            raise ValueError("there's not only one '/' at the string or another symbols except - and /")
            else:
                try:
                    self._a = int(a)
                    self._b = b
                except ValueError:
                    raise ValueError("absolut bulshit number")


    @staticmethod
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    def __lt__(self, other):
        if isinstance(other, R):
            self.abbreviate()
            other.abbreviate()
            if self._b == other._b:
                return self._a < other._a
            return self._b < other._b
        else:
            raise ValueError("other is not R class, operation < is unsupported")

    def __gt__(self, other):
        if isinstance(other, R):
            self.abbreviate()
            other.abbreviate()
            if self._b == other._b:
                return self._a > other._a
            return self._b > other._b
        else:
            raise ValueError("other is not R class, operation > is unsupported")

    def __eq__(self, other):
        if isinstance(other, R):
            self.abbreviate()
            other.abbreviate()
            if self._b == other._b and self._a == other._a:
                return True
            return False
        else:
            raise ValueError("other is not R class, operation == is unsupported")



    @staticmethod
    def set_by_sting(string):
        assert isinstance(string, str)
        if "/" in string:
            for j in range(len(string)):
                if string[j] == "/":
                    n = int(string[0: j])
                    d = int(string[j + 1:])
                    return R(n, d)
        else:
            try:
                return R(int(string))
            except ValueError:
                raise ValueError("monkey test has been failed")
        # else:
        #     try:
        #         return I(int(string))
        #     except ValueError:
        #         raise ValueError("it isn't R or I, monkey!!!!")


    def abbreviate(self):
        gcd = self.gcd(self._a, self._b)
        self._a = self._a // gcd
        self._b = self._b // gcd


    def __add__(self, other):

        if type(other) == int:
            new_a = self._a + other * self._b
            result = R(new_a, self._b)
            result.abbreviate()
            return result

        elif type(other) == I:
            new_a = self._a + other.num * self._b
            result = R(new_a, self._b)
            result.abbreviate()
            return result

        elif type(other) == R:
            new_a = self._a * other._b + self._b * other._a
            new_b = self._b * other._b
            result = R(new_a, new_b)
            result.abbreviate()
            return result
        else:
            raise AssertionError

    def __mul__(self, other):
        if type(other) == int:
            new_a = self._a * other
            result = R(new_a, self._b)
            result.abbreviate()
            return result

        elif type(other) == I:
            new_a = self._a * other.num
            result = R(new_a, self._b)
            result.abbreviate()
            return result

        elif type(other) == R:
            new_a = self._a * other._a
            new_b = self._b * other._b
            result = R(new_a, new_b)
            result.abbreviate()
            return result
        else:
            raise AssertionError

    def __sub__(self, other):
        if type(other) == int:
            result = R(self._a - other * self._b, self._b)
            result.abbreviate()
            return result

        elif type(other) == I:
            result = R(self._a - other.num * self._b, self._b)
            result.abbreviate()
            return result

        elif type(other) == R:
            new_a = self._a * other._b - self._b * other._a
            new_b = self._b * other._b
            result = R(new_a, new_b)
            result.abbreviate()
            return result
        else:
            raise AssertionError

    def __call__(self, typical_form=True):
        if typical_form:
            return self._a / self._b
        length =10^len((self._a % self._b) / self._b)
        return R((self._a // self_b) * self._b * (self._a % self_b) * length, length)

    def __getitem__(self, key):
        if key == "n":
            return self._a
        elif key == "d":
            return self._b
        else:
            raise KeyError("Invalid key and you :)))))")

    def __setitem__(self, key, value):
        assert type(value) == int
        if key == "n":
            self._a = value
        elif key == "d":

            self._b = value
        else:
            raise KeyError("Invalid key and you :)))))")


    def __str__(self):
        # if self._a % self._b == 0:
        #     i = I(self._a // self._b)
        #     return i.__str__()
        return f'R {self._a} / {self._b}'


class I:
    def __init__(self, num):
        assert type(num) == int
        self.num = num


    def __add__(self, other):
        if type(other) == int:
            return I(self.num + other)

        elif type(other) == I:
            return I(self.num + other.num)

        elif type(other) == R:
            new_a = other._a + self.num * other._b
            result = R(new_a, other._b)
            result.abbreviate()
            return result
        else:
            raise TypeError("addition isn't supported between this two classes")

    def __mul__(self, other):
        if type(other) == I:
            return I(self.num * other.num)
        elif type(other) == int:
            return I(self.num * other)
        elif type(other) == R:
            result = R(self.num * other._a, other._b)
            result.abbreviate()
            return result


    def __sub__(self, other):
        if type(other) == R:
            result = R(self.num * other._b - other._a, other._b)
            result.abbreviate()
            return result

        elif type(other) == int:
            return I(self.num - other)

        elif type(other) == I:
            return I(self.num - other.num)


    def __str__(self):
        return f"I {self.num}"




if __name__ == "__main__":
    print(R("55/43"))

    print(R(7, 2) > R(7, 1))

    print(R(8, 1) > R(7, 1))

    print(R(8, 1) > R(7, 2))

    print(R(6, 1) > R(7, 1))
    ########
    print(R(7, 2) < R(7, 1))

    print(R(8, 1) < R(7, 1))

    print(R(8, 1) < R(7, 2))

    print(R(6, 1) < R(7, 1))
    #####
    print(R(6, 2) == R(7, 2))

    print(R(7, 2) == R(7, 2))

    print(R(6, 2) == R(6, 1))

    print(R(6, 2) == R(12, 4))

    r1 = R(6, 2)
    r2 = R(7, 1)
    r3 = R(7, 2)
    lst_R = [r1, r2, r3]
    tuple_R = tuple(lst_R)
    print(tuple_R)