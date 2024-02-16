class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def perimeter(self):
        result = 2 * self.a + 2 * self.b
        return result
    def area(self):
        result = self.a * self.b
        return result
    def __str__(self) -> str:
        return f"Rectangle: a={self.a} b={self.b}"