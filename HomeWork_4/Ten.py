from One import One
from Zero import Zero
import turtle
class Ten:
    def __init__(self):
        self.one = One()
        self.zero = Zero()
        self.position = (0, 0)


    def set_position(self, x, y):
        self.position = (x, y)

    def __calculate_abs_position(self):
        self.one.set_position(self.position[0] - 8, self.position[1])
        self.zero.set_position(self.position[0] + 8, self.position[1])

    def draw(self):
        self.__calculate_abs_position()

        self.one.draw()
        self.zero.draw()

if __name__ == '__main__':
    one_obj = Ten()
    one_obj.set_position(130, -213)
    one_obj.draw()
    turtle.mainloop()