from Triangle3 import Triangle
from turtle import *

speed(0)
t = Triangle(100, 100, 100, 0)
t.set_random_color()
t.draw()

t.set_pivot(*t.get_bisec_centre())
# поворот
for i in range(1, 360, 10):
    t.set_random_color()
    t.set_pivot(50, 50)
    t.rotate(i)
    t.draw()