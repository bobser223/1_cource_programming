class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def perimeter(self):
        result = 2 * self.a + 2 * self.b
        return result
    def square(self):
        result = self.a * self.b
        return result
