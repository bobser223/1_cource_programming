import turtle
from vecSum import vecSum

class Four:
    def __init__(self):
        self._position = (0, 0)
        self.__v1 = (-5, 0)
        self.__v2 = (0, 20)
        # up pos
        self.__v3 = (5, 0)
        self.__v4 = (0, 20)
        self.__v5 = (0, -40)



    def set_position(self, x, y):
        self._position = (x, y)


    def __calculate_abs_position(self):
        absV1 = vecSum(self.__v1, self._position)
        absV2 = vecSum(self.__v2, absV1)

        absV3 = vecSum(self.__v3, self._position)
        absV4 = vecSum(self.__v4, absV3)
        absV5 = vecSum(self.__v5, absV4)
        return absV1, absV2, absV3, absV4, absV5


    def draw(self):
        abs_vectors = self.__calculate_abs_position()
        turtle.penup()
        turtle.goto(self._position)
        turtle.pendown()
        turtle.goto(abs_vectors[0])
        turtle.goto(abs_vectors[1])
        turtle.penup()
        turtle.goto(self._position)
        turtle.pendown()
        turtle.goto(abs_vectors[2])
        turtle.goto(abs_vectors[3])
        turtle.goto(abs_vectors[4])
        turtle.penup()

if __name__ == '__main__':
    t = Four()
    t.set_position(345, -67)
    t.draw()
