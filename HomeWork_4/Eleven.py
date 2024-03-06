from One import One
import turtle

class Eleven:
    def __init__(self):
        self.one1 = One()
        self.one2 = One()
        self.position = (0, 0)


    def set_position(self, x, y):
        self.position = (x, y)

    def __calculate_abs_position(self):
        self.one1.set_position(self.position[0] - 8, self.position[1])
        self.one2.set_position(self.position[0] + 8, self.position[1])

    def draw(self):
        self.__calculate_abs_position()

        self.one1.draw()
        self.one2.draw()

if __name__ == '__main__':
    one_obj = Eleven()
    one_obj.set_position(130, -213)
    one_obj.draw()
    turtle.mainloop()