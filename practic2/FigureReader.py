from Triangle import Triangle
from Rectangle import Rectangle
from Trapeze import Trapeze
from Circle import Circle
from Parallelogram import Parallelogram
from Triangularpyramid import Triangularpyramid
from TriangularPrism import TriangularPrism
from RectangularParallelepiped import RectangularParallelepiped
from QuadrangularPyramid import QuadrangularPyramid
from Cone import Cone
from Circle import Circle
from Ball import Ball
class FigureReader:
    def __init__(self, file_name):
        self.file_name = file_name
    def read(self):
        figures = []
        with open(self.file_name) as f:
            for line in f:
                data = line.split()
                type = data[0]
                try:
                    if type == "Triangle":
                        a, b, c = [float(el) for el in data[1:]]
                        triangle = Triangle(a, b, c)
                        figures.append(triangle)
                    elif type == "Rectangle":
                        a, b = [float(el) for el in data[1:]]
                        rectangle = Rectangle(a, b)
                        figures.append(rectangle)
                    elif type == "Parallelogram":
                        a, b, h = [float(el) for el in data[1:]]
                        parallelogram = Parallelogram(a, b, h)
                        figures.append(parallelogram)
                        pass
                    elif type == "Circle":
                        r = float(data[1])
                        circle = Circle(r)
                        figures.append(circle)
                        pass
                    elif type == "Trapeze":
                        a, b, c, d = [float(el) for el in data[1:]]
                        trapeze = Trapeze(a, b, c, d)
                        figures.append(trapeze)
                    elif type == "TriangularPyramid":
                        a, h = [float(el) for el in data[1:]]
                        triangularpyramid = Triangularpyramid(a, h)
                        figures.append(triangularpyramid)
                    elif type == "TriangularPrism":
                        a, b, c, l = [float(el) for el in data[1:]]
                        triangularprism = TriangularPrism(a, b, c, l)
                        figures.append(triangularprism)
                    elif type == "RectangularParallelepiped":
                        a, b, c = [float(el) for el in data[1:]]
                        rp = RectangularParallelepiped(a, b, c)
                        figures.append(rp)
                    elif type == "QuadrangularPyramid":
                        a, b, h = [float(el) for el in data[1:]]
                        qp = QuadrangularPyramid(a, b, h)
                        figures.append(qp)
                    elif type == "Cone":
                        r, h = [float(el) for el in data[1:]]
                        cone = Cone(r, h)
                        figures.append(cone)
                    elif type == "Circle":
                        r = float(data[1])
                        circle = Circle(r)
                        figures.append(circle)
                    elif type == "Ball":
                        r = float(data[1])
                        ball = Ball(r)
                        figures.append(ball)
                except AssertionError:
                    pass
        return figures



