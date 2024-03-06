from One import One
from Two import Two
import turtle

class Twelve:
    def __init__(self):
        self.one = One()
        self.two = Two()
        self.position = (0, 0)


    def set_position(self, x, y):
        self.position = (x, y)

    def __calculate_abs_position(self):
        self.one.set_position(self.position[0] - 8, self.position[1])
        self.two.set_position(self.position[0] + 8, self.position[1])

    def draw(self):
        self.__calculate_abs_position()

        self.one.draw()
        self.two.draw()

if __name__ == '__main__':
    one_obj = Twelve()
    one_obj.set_position(130, -213)
    one_obj.draw()
    turtle.mainloop()