import turtle
from random import randint
from Triangle import Triangle

triangles = []
for i in range(100):
    x1 = (randint(-100, 100))
    x2 = (randint(-100, 100))
    y1 = randint(-100, 100)
    y2 = randint(-100, 100)
    t = Triangle(x1, y1, x2, y2)

    r = randint(15, 255)
    g = randint(15, 255)
    b = randint(15, 255)
    color = r << 16 | g << 8 | b
    t.set_color("#" + (str(hex(color)))[2:])
    triangles.append(t)


for t in triangles:
    t.draw()

turtle.mainloop()
    