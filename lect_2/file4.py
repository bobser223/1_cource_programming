import copy
import randit from random
# triangle_id = 0
class Triangle:
    triangle_id = 0 # татичне поле класу

    @staticmethod
    def get_triangle_id():
        return Triangle.triangle_id

    @staticmethod
    def gen_triangle_id():
        return randit(1, 10000000)

    def __init__(self, a, b = None, c = None):
        # global triangle_id
        if isinstance(a, Triangle):
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            self.a = a
            self.b = b
            self.c = c
        self.id = Triangle.triangle_id
        Triangle.triangle_id += 1
    # def __init__(self, otherTriangle):
    #     global triangle_id
    #     self.a = otherTriangle.a
    #     self.b = otherTriangle.b
    #     self.c = otherTriangle.c
    #     self.id = triangle_id
    #     triangle_id += 1
    # def perimeter(self):
    #     return (self.a + self.b + self.c) / 2

    def area(self):
        p = self.perimeter()
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


    def show(self):
        print("Triangle",self.id, self.a, self.b, self.c)



if __name__ == "__main__":
    t = Triangle(3, 4, 5)
    t3 = Triangle(t)
    # t.show()
    # t3.show()
    print(Triangle.triangle_id)
    print(t.triangle_id)
    print(t3.triangle_id)