from Triangle import Triangle
from Rectangle import Rectangle
from Trapeze import Trapeze
class FigureReader:
    def __init__(self, file_name):
        self.file_name = file_name
    def read(self):
        figures = []
        with open(self.file_name) as f:
            for line in f:
                data = line.split()
                #print(data)
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
                        pass
                    elif type == "Circle":
                        pass
                    elif type == "Trapeze":
                        a, b, c, d = [float(el) for el in data[1:]]
                        trapeze = Trapeze(a, b, c, d)
                        figures.append(trapeze)
                except AssertionError:
                    pass
        return figures



