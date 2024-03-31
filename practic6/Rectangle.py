from Figure import Figure

from math import sin, cos, radians
import turtle

class Rectangle(Figure):
    def __init__(self, x1, y1):
        super().__init__()
        self.vertex1 = (x1, y1)

    def draw(self):
        v1 = self.calc_abs_pos((self.vertex1[0], 0))
        v2 = self.calc_abs_pos(self.vertex1)
        v3 = self.calc_abs_pos((0, self.vertex1[1]))
        turtle.color(self.color)
        turtle.up()
        turtle.setpos(self.move())
        turtle.down()
        turtle.goto(v1)
        turtle.goto(v2)
        turtle.goto(v3)
        turtle.setpos(self.move())
        turtle.up()
        turtle.color(Rectangle.default_color)

if __name__ == '__main__':
    rectangle = Rectangle(100, 100)
    rectangle.draw()


    turtle.mainloop()