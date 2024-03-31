
from Figure import Figure

from math import sin, cos, radians
import turtle

class Circle(Figure):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def draw(self):
        s = self.r * self.scale[0]
        v1 =self.position[0],  self.position[1] - s
        turtle.color(self.color)
        turtle.up()
        turtle.setpos(*v1)
        turtle.down()
        turtle.circle(s)
        turtle.up()
        turtle.color(Circle.default_color)

if __name__ == '__main__':
    rectangle = Circle(100)
    rectangle.draw()


    turtle.mainloop()
