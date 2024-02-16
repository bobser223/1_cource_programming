from FigureReader import FigureReader
if __name__ == "__main__":
    reader = FigureReader("input.txt")
    figures = reader.read()
    for figure in figures:
        print(figure, "Area = ", figure.square())

    pass



# from Triangle import Triangle
# from Rectangle import Rectangle
# from Trapeze import Trapeze
# try:
#     eq = Triangle(3, 4, 5)
#     print(eq.perimeter())
#     print(eq.square())
# except AssertionError:
#     print("це не трикутник")
# eq1 = Rectangle(2, 3)
# print(eq1.perimeter())
# print(eq1.square())
#
# try:
#     eq2 = Trapeze(2, 2, 3, 3)
#     print(eq2.perimeter())
#     print(eq2.square())
# except AssertionError:
#     print("це не трапеція")