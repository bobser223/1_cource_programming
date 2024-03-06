import turtle
from math import sin, cos, radians
import time

class Arrow_min:
    def __init__(self):
        self._length = (0, 200)
        self._fi_degree = 0
        self.t = turtle.Turtle()

    def set_length(self, x, y):
        self._length = (x, y)


    def set_fi_degree(self, fi):
        self._fi_degree = fi

    @staticmethod
    def multMatrixVector(M, v):
        turnedVector1 = [0, 0]
        turnedVector1[0] = M[0][0] * v[0] + M[0][1] * v[1]
        turnedVector1[1] = M[1][0] * v[0] + M[1][1] * v[1]
        return turnedVector1

    def turnArrow(self):
        fi = radians(self._fi_degree)
        fiMatrix = [
            [cos(fi), -sin(fi)],
            [sin(fi), cos(fi)]
        ]
        turnedVector = self.multMatrixVector(fiMatrix, self._length)
        return turnedVector

    def draw(self):
        self.t.color("red")
        curVec = self.turnArrow()
        self.t.penup()
        self.t.goto(0,0)
        self.t.pendown()
        self.t.goto(curVec)


if __name__ == "__main__":
    arr = Arrow()
    arr.set_fi_degree(90)
    arr.draw()
    while True:
        for fi in range(360, 0, -5):
            self.__arrow.set_fi_degree(fi)
            time.sleep(1)