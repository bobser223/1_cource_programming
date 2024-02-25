from Triangle import Triangle
from random import randint, choices
import ast
import turtle

def random_color():
    # colors = []
    # with open('colors.txt', 'r') as f:
    #     for line in f:
    #         line = line.strip()
    #         colors.append((line))
    # return colors[randint(0, len(colors) - 1)]
    a = str(randint(0, 255))
    b = str(randint(0, 255))
    c = str(randint(0, 255))
    color = a + b + c
    color = str(hex(int(color)))[2:]
    color = color.upper()
    if len(color) != 6:
        return random_color()
    return "#" + color
    # return str([randint(0, 255), randint(0, 255), randint(0, 255)])
    # return "black"

if __name__ == '__main__':
    turtle.speed(0)
    # while True:
    for _ in range(100):
        triangle = Triangle(randint(-200, 200), randint(-200, 200), randint(-200, 200), randint(-200, 200))
        triangle.set_position(randint(-200, 200), randint(-200, 200))
        triangle.set_color(random_color())
        triangle.draw()
    turtle.mainloop()