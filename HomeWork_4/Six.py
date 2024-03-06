import turtle
from vecSum import vecSum

class Six:
    def __init__(self):
        self._position = (0, 0)
        self.__v1 = (-5, 0)
        self.__v2 = (0, 20)
        self.__v3 = (10, 0)
        self.__v4 = (0, -5)
        # pos
        self.__v5 = (5, 0)
        self.__v6 = (0, -20)
        self.__v7 = (-10, 0)
        self.__v8 = (0, 20)


    def set_position(self, x, y):
        self._position = (x, y)


    def __calculate_abs_position(self):
        absV1 = vecSum(self.__v1, self._position)
        absV2 = vecSum(self.__v2, absV1)
        absV3 = vecSum(self.__v3, absV2)
        absV4 = vecSum(self.__v4, absV3)
        # pos
        absV5 = vecSum(self.__v5, self._position)
        absV6 = vecSum(self.__v6, absV5)
        absV7 = vecSum(self.__v7, absV6)
        absV8 = vecSum(self.__v8, absV7)
        return absV1, absV2, absV3, absV4, absV5, absV6, absV7, absV8

    def draw(self):
        abs_vectors = self.__calculate_abs_position()
        turtle.penup()
        turtle.goto(self._position)
        turtle.pendown()
        turtle.goto(abs_vectors[0])
        turtle.goto(abs_vectors[1])
        turtle.goto(abs_vectors[2])
        turtle.goto(abs_vectors[3])
        turtle.penup()
        turtle.goto(self._position)
        turtle.pendown()
        turtle.goto(abs_vectors[4])
        turtle.goto(abs_vectors[5])
        turtle.goto(abs_vectors[6])
        turtle.goto(abs_vectors[7])
        turtle.penup()

if __name__ == '__main__':
    t = Six()
    t.set_position(345, -67)
    t.draw()
