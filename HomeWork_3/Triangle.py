from math import sin, cos, pi, radians
import turtle

class Triangle:
    default_color = "DeepPink3"

    def __init__(self, x1, y1, x2, y2):
        self._vertex1 = (x1, y1)
        self._vertex2 = (x2, y2)
        self.color = Triangle.default_color
        self.position = (0, 0)
        self.rotation = 0
        self.scale = (1, 1)
        self._pivot = (0, 0)

    def set_pivot(self, pivot_x, pivot_y):
        self._pivot = (pivot_x, pivot_y)

    def set_position(self, x, y):
        self.position = (x, y)
        self._vertex1, self._vertex2 = set_curr_pos()


    def set_curr_possition(self):
        currV1 = (self._vertex1[0] + self.position[0], self._vertex1[1] + self.position[1])
        currV2 = (self._vertex2[0] + self.position[0], self._vertex2[1] + self.position[1])
        return currV1, currV2


    def set_scale(self, scale_x, scale_y):
        self.scale = (scale_x, scale_y)

    def vector_module(self, vector):
        sum = 0
        for el in vector:
            sum += el ** 2
        return sum ** 0.5



    def get_incenter(self):
        ax, ay = self.position
        bx, by = self._vertex1
        cx, cy = self._vertex2
        C = self.vector_module(((ax - bx), (ay - by)))
        A = self.vector_module(((bx - cx), (by - cy)))
        B = self.vector_module(((cx - ax), (cy - ay)))
        ABC = A + B + C
        x = (ax * A + bx * B + cx * C) / ABC
        y = (ay * A + by * B + cy * C) / ABC
        return x, y

    def get_centroid(self):
        ax, ay = self.position
        bx, by = self._vertex1
        cx, cy = self._vertex2
        x = (ax + bx + cx) / 3
        y = (ay + by + cy) / 3
        return x, y

    def set_color(self, color):
        self.color = color

    def set_rotation(self, rotation):
        self.rotation = rotation

    def set_rotation_degree(self, degree):
        self.rotation = radians(degree)

    def rotationMatrix(self):
        fi = self.rotation
        fiMatrix = [
            [cos(fi), -sin(fi)],
            [sin(fi), cos(fi)]
        ]
        return fiMatrix

    @staticmethod
    def multMatrixVector(M, v):
        turnedVertex1 = (M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1])
        return turnedVertex1

    def move(self, dx, dy):
        self.position = (self.position[0] + dx, self.position[1] + dy)

    def scaleVertex(self, vertor):
        return (self.scale[0] * vertor[0], self.scale[1] * vertor[1])


    def rotateVertex(self, vec):
        return self.multMatrixVector(self.rotationMatrix(), vec)


    def calc_changes_relative_to_pivot(self):
        l, m = self._pivot

        normPos = (self.position[0] - l, self.position[1] - m)
        normV1 = (self._vertex1[0] - l, self._vertex1[1] - m)
        normV2 = (self._vertex2[0] - l, self._vertex2[1] - m)

        scaledPos = self.scaleVertex(normPos)
        scaledV1 = self.scaleVertex(normV1)
        scaledV2 = self.scaleVertex(normV2)

        rotatedPos = self.rotateVertex(scaledPos)
        rotatedV1 = self.rotateVertex(scaledV1)
        rotatedV2 = self.rotateVertex(scaledV2)

        changedPos = (rotatedPos[0] + l, rotatedPos[1] + m)
        changedVertex1 = (rotatedV1[0] + l, rotatedV1[1] + m)
        changedVertex2 = (rotatedV2[0] + l, rotatedV2[1] + m)

        return changedPos, changedVertex1, changedVertex2


    def draw(self):
        pos, v1, v2 = self.calc_changes_relative_to_pivot()
        turtle.color(self.color)
        turtle.up()
        turtle.setpos(*pos)
        turtle.down()
        turtle.goto(*v1)
        turtle.goto(*v2)
        turtle.setpos(*pos)
        turtle.up()
        turtle.color(Triangle.default_color)



if __name__ == '__main__':
    turtle.speed(0)
    triangle = Triangle(100, 100, 100, 0)
    triangle.set_scale(3, 3)
    triangle.set_pivot(*triangle.get_incenter())
    for degree in range(0, 366, 6):
        triangle.set_rotation_degree(degree)
        triangle.draw()

    turtle.clear()

    triangle.set_pivot(*triangle.get_centroid())
    scale = 1
    while scale < 8:
        triangle.set_scale(scale, scale)
        triangle.draw()
        scale += 1


    turtle.mainloop()