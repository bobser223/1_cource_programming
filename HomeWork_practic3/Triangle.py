from math import sin, cos, pi, radians
import turtle

class Triangle:
    default_color = "DeepPink3"

    def __init__(self, x1, y1, x2, y2):
        self.vertex1 = (x1, y1)
        self.vertex2 = (x2, y2)
        self.color = Triangle.default_color
        self.position = (0, 0)

    def set_position(self, x, y):
        self.position = (x, y)

    def set_color(self, color):
        self.color = color

    def calc_abs_pos(self):
        v1 = (self.position[0] + self.vertex1[0],
              self.position[1] + self.vertex1[1])
        v2 = (self.position[0] + self.vertex2[0],
              self.position[1] + self.vertex2[1])
        return v1, v2

    def draw(self):
        v1, v2 = self.calc_abs_pos()
        turtle.color(self.color)
        turtle.up()
        turtle.setpos(*self.position)
        turtle.down()
        turtle.goto(*v1)
        turtle.goto(*v2)
        turtle.setpos(*self.position)
        turtle.up()
        turtle.color(Triangle.default_color)

    def turn(self, fi):
        fiMatrix = [[cos(fi), -sin(fi)],
                    [sin(fi), cos(fi)]]

        turnedVertex1 = [0, 0]
        turnedVertex2 = [0, 0]

        turnedVertex1[0] = fiMatrix[0][0] * self.vertex1[0] + fiMatrix[0][1] * self.vertex1[1]
        turnedVertex1[1] = fiMatrix[1][0] * self.vertex1[0] + fiMatrix[1][1] * self.vertex1[1]
        turnedVertex2[0] = fiMatrix[0][0] * self.vertex2[0] + fiMatrix[0][1] * self.vertex2[1]
        turnedVertex2[1] = fiMatrix[1][0] * self.vertex2[0] + fiMatrix[1][1] * self.vertex2[1]
        # self.vertex1 = turnedVertex1
        # self.vertex2 = turnedVertex2
        return Triangle(turnedVertex1[0],  turnedVertex1[1], turnedVertex2[0], turnedVertex2[1])



if __name__ == '__main__':
    turtle.speed(0)
    triangle = Triangle(100, 100, 100, 0)
    triangle.draw()
    # turtle.clear()
    for degree in range(3, 363, 3):
        (triangle.turn(radians(degree))).draw()
        turtle.clear()



    # triangle.set_color("#38915F")
    # for i in range(100):
    #     turtle.clear()
    #     triangle.set_position(-2 * i, -i)
    #     triangle.draw()


    turtle.mainloop()