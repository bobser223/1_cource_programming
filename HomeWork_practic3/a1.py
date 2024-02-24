from random import randint, choices
import turtle
from Triangle import Triangle


colors = []
with open('colors.txt', 'r') as f:
    for line in f:
        line = line.strip()
        colors.append((line))

for i in range(len(colors)):
    print(i)
    turtle.color(colors[i])
