import turtle
from math import radians, cos, sin, sqrt
class Stick:
    def __init__(self):
        self.__lil_stick1 = (0, 300)
        self.__lil_stick2 = (0, 290)
        self._fi_degree = 0
        self.__og_stick1 = (0, 300)
        self.__og_stick2 = (0, 280)
        self.t = turtle.Turtle()
    @staticmethod
    def multMatrixVector(M, v):
        turnedVector1 = [0, 0]
        turnedVector1[0] = M[0][0] * v[0] + M[0][1] * v[1]
        turnedVector1[1] = M[1][0] * v[0] + M[1][1] * v[1]
        return turnedVector1

    def set_fi_degree(self, fi):
        self._fi_degree = fi

    def turn(self, v1, v2):
        fi = radians(self._fi_degree)
        fiMatrix = [
            [cos(fi), -sin(fi)],
            [sin(fi), cos(fi)]
        ]
        turned_lil1 = self.multMatrixVector(fiMatrix, v1)
        turned_lil2 = self.multMatrixVector(fiMatrix, v2)
        return turned_lil1, turned_lil2

    def draw_lil(self):
        turned_lil1, turned_lil2 = self.turn(self.__lil_stick1, self.__lil_stick2)
        self.t.penup()
        self.t.goto(turned_lil2)
        self.t.pendown()
        self.t.goto(turned_lil1)
        self.t.penup()

    def draw_og(self):
        turned_lil1, turned_lil2 = self.turn(self.__og_stick1, self.__og_stick2)
        self.t.penup()
        self.t.goto(turned_lil2)
        self.t.pendown()
        self.t.goto(turned_lil1)
        self.t.penup()


if __name__ == '__main__':
    stick = Stick()
    stick.draw_lil()
    stick.set_fi_degree(55)
    stick.draw_og()
    turtle.mainloop()

