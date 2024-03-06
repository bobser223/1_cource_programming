import turtle
from math import sin, cos, radians
import time

class Arrow:
    def __init__(self):
        self._length = (0, 170)
        self._fi_degree = 0

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
        curVec = self.turnArrow()
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        turtle.goto(curVec)


if __name__ == "__main__":
    arr = Arrow()
    arr.set_fi_degree(90)
    arr.draw()
    while True:
        for fi in range(360, 0, -5):
            self.__arrow.set_fi_degree(fi)
            time.sleep(1)



