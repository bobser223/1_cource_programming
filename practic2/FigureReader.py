from Triangle import Triangle
class FigureReader:
    def __init__(self, file_name):
        self.file_neme = file_name
    def read(self):
        figures = []
        with open(self.file_neme) as f:
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
                        pass
                    elif type == "Parallelogram":
                        pass
                    elif type == "Circle":
                        pass
                    elif type == "Trapeze":
                        pass
                except AssertionError:
                    pass
        return figures



