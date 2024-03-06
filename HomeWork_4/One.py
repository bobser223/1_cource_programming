import turtle
from vecSum import vecSum


class One:
    def __init__(self):
        self._position = (0, 0)
        self.__v1 = (5, 0)
        self.__v2 = (0, 20)
        self.__v3 = (-10, -15)
        self.__v4 = (0, -20)

    def set_position(self, x, y):
        self._position = (x, y)



    def __calculate_abs_position(self):
        absV1 = vecSum(self.__v1, self._position)
        absV2 = vecSum(self.__v2, absV1)
        absV3 = vecSum(self.__v3, absV2)
        absV4 = vecSum(self.__v4, absV1)
        return absV1, absV2, absV3, absV4

    def draw(self):
        abs_vectors = self.__calculate_abs_position()
        turtle.penup()
        turtle.goto(abs_vectors[0])
        turtle.pendown()
        turtle.goto(abs_vectors[1])
        turtle.goto(abs_vectors[2])
        turtle.penup()
        turtle.goto(abs_vectors[0])
        turtle.pendown()
        turtle.goto(abs_vectors[3])
        turtle.penup()

if __name__ == '__main__':
    one_obj = One()
    one_obj.set_position(130, -213)
    one_obj.draw()
    turtle.mainloop()