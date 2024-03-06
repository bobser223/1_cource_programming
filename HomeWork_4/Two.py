import turtle
from vecSum import vecSum

class Two:
    def __init__(self):
        self._position = (0, 0)
        self.__v1 = (5, 0)
        self.__v2 = (0, 20)
        self.__v3 = (-10, 0)
        self.__v4 = (0, -10)
        # up
        # pos
        self.__v5 = (-5, 0)
        self.__v6 = (0, -20)
        self.__v7 = (10, 0)
        self.__v8 = (0, 10)

    def set_position(self, x, y):
        self._position = (x, y)



    def __calculate_abs_position(self):
        absV1 = vecSum(self._position, self.__v1)
        absV2 = vecSum(absV1, self.__v2)
        absV3 = vecSum(absV2, self.__v3)
        absV4 = vecSum(absV3, self.__v4)

        absV5 = vecSum(self._position, self.__v5)
        absV6 = vecSum(absV5, self.__v6)
        absV7 = vecSum(absV6, self.__v7)
        absV8 = vecSum(absV7, self.__v8)

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
    two = Two()
    two.set_position(204, -67)
    two.draw()
    turtle.mainloop()