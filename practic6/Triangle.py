from Figure import Figure

from math import sin, cos, radians
import turtle

class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.vertex1 = (x1, y1)
        self.vertex2 = (x2, y2)

    def draw(self):
        v1 = self.calc_abs_pos(self.vertex1)
        v2 = self.calc_abs_pos(self.vertex2)
        turtle.color(self.color)
        turtle.up()
        turtle.setpos(*self.move())
        turtle.down()
        turtle.goto(*v1)
        turtle.goto(*v2)
        turtle.setpos(*self.move())
        turtle.up()
        turtle.color(Triangle.default_color)

if __name__ == '__main__':
    turtle.speed(0)
    triangle = Triangle(100, 100, 100, 0)
    triangle.draw()
    turtle.clear()

    triangle.set_color("#38915F")
    for i in range(3, 363, 3):
        turtle.clear()
        triangle.set_rotation_degree(i)
        triangle.draw()