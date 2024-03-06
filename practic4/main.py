from Triangle import Triangle
from random import randint, choices
import ast
import turtle

def random_color():
    a = str(randint(0, 255))
    b = str(randint(0, 255))
    c = str(randint(0, 255))
    color = a + b + c
    color = str(hex(int(color)))[2:]
    color = color.upper()
    if len(color) != 6:
        return random_color()
    return "#" + color

if __name__ == '__main__':
    turtle.speed(0)
    # while True:
    for _ in range(100):
        triangle = Triangle(randint(-200, 200), randint(-200, 200), randint(-200, 200), randint(-200, 200))
        triangle.set_position(randint(-200, 200), randint(-200, 200))
        triangle.set_color(random_color())
        triangle.draw()