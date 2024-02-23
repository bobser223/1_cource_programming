from random import randint
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)
# r = 255
# g = 0
# b = 255
color = r << 16 | g << 8 | b
print(hex(color))