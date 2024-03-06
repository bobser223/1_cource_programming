import turtle
from math import sin, cos, radians
from Zero import Zero
from One import One
from Two import Two
from Three import Three
from Four import Four
from Five import Five
from Six import Six
from Seven import Seven
from Eight import Eight
from Nine import Nine
from Ten import Ten
from Eleven import Eleven
from Twelve import Twelve
from Arrow import Arrow
import time
from Arrow_min import Arrow_min
from Arrow_hour import Arrow_hour

class Dial:

    def __init__(self):
        self.radius = 300
        self.position = (0, 0)
        self.__invisibleVector = (265, 0)
        self.__zero = Zero()
        self.__one = One()
        self.__two = Two()
        self.__three = Three()
        self.__four = Four()
        self.__five = Five()
        self.__six = Six()
        self.__seven = Seven()
        self.__eight = Eight()
        self.__nine = Nine()
        self.__ten = Ten()
        self.__eleven = Eleven()
        self.__twelve = Twelve()
        self.__arrow = Arrow()
        self.__arrow_min = Arrow_min()
        self.__arrow_hour = Arrow_hour()

    @staticmethod
    def multMatrixVector(M, v):
        turnedVector1 = [0, 0]
        turnedVector1[0] = M[0][0] * v[0] + M[0][1] * v[1]
        turnedVector1[1] = M[1][0] * v[0] + M[1][1] * v[1]
        return turnedVector1

    def turnInvisibleVector(self, fi_degree):
        fi = radians(fi_degree)
        fiMatrix = [
            [cos(fi), -sin(fi)],
            [sin(fi), cos(fi)]
        ]
        turnedVector = self.multMatrixVector(fiMatrix, self.__invisibleVector)
        return turnedVector

    def drawNumbers(self): # Хотілося б циклом, але анріал
        fi = 30
        self.__three.set_position(*self.__invisibleVector)
        self.__three.draw()
        self.__two.set_position(*self.turnInvisibleVector(fi))
        self.__two.draw()
        fi += 30
        self.__one.set_position(*self.turnInvisibleVector(fi))
        self.__one.draw()
        fi += 30
        self.__twelve.set_position(*self.turnInvisibleVector(fi))
        self.__twelve.draw()
        fi += 30
        self.__eleven.set_position(*self.turnInvisibleVector(fi))
        self.__eleven.draw()
        fi += 30
        self.__ten.set_position(*self.turnInvisibleVector(fi))
        self.__ten.draw()
        fi += 30
        self.__nine.set_position(*self.turnInvisibleVector(fi))
        self.__nine.draw()
        fi += 30
        self.__eight.set_position(*self.turnInvisibleVector(fi))
        self.__eight.draw()
        fi += 30
        self.__seven.set_position(*self.turnInvisibleVector(fi))
        self.__seven.draw()
        fi += 30
        self.__six.set_position(*self.turnInvisibleVector(fi))
        self.__six.draw()
        fi += 30
        self.__five.set_position(*self.turnInvisibleVector(fi))
        self.__five.draw()
        fi += 30
        self.__four.set_position(*self.turnInvisibleVector(fi))
        self.__four.draw()


    def drawCholck(self):
        currentPosition = (self.position[0], self.position[1] - self.radius)
        turtle.penup()
        turtle.goto(currentPosition)
        
        turtle.pendown()
        turtle.circle(self.radius)
        turtle.penup()

        self.drawNumbers()
        self.showTime()
        turtle.done()


    def showTime(self):
        while True:
            for alpha in range(360, 0, -30):
                self.__arrow_hour.set_fi_degree(alpha)
                self.__arrow_hour.draw()
                for theta in range(360, 0, -5):
                    self.__arrow_min.set_fi_degree(theta)
                    self.__arrow_min.draw()
                    for fi in range(360, 0, -5):
                        self.__arrow.set_fi_degree(fi)
                        self.__arrow.draw()
                        time.sleep(1)
                        self.__arrow.t.undo()
                    self.__arrow_min.t.undo()
                self.__arrow_hour.t.undo()




if __name__ == '__main__':
    dial = Dial()
    dial.drawCholck()
    dial.showTime()