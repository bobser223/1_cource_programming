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

    # def rotate_around_point(self, angle_deg, point):
    #     # Перетворюємо кут з градусів у радіани
    #     angle_rad = radians(angle_deg)
    #
    #     # Обчислюємо вектор переміщення до точки повороту
    #     dx = self.position[0] - point[0]
    #     dy = self.position[1] - point[1]
    #
    #     # Використовуємо матрицю повороту для обчислення нового положення вектора переміщення
    #     rotated_dx = dx * cos(angle_rad) - dy * sin(angle_rad)
    #     rotated_dy = dx * sin(angle_rad) + dy * cos(angle_rad)
    #
    #     # Встановлюємо нове положення трикутника, зміщуючи його до початкової точки повороту
    #     # і додаючи обернений вектор переміщення
    #     self.position = (point[0] + rotated_dx, point[1] + rotated_dy)

        # Збільшуємо кут повороту трикутника
        self.rotation += angle_radif __name__ == '__main__':
    turtle.speed(0)
    # while True:
    for _ in range(100):
        triangle = Triangle(randint(-200, 200), randint(-200, 200), randint(-200, 200), randint(-200, 200))
        triangle.set_position(randint(-200, 200), randint(-200, 200))
        triangle.set_color(random_color())
        triangle.draw()
    turtle.mainloop()