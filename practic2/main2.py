from FigureReader2 import FigureReader2
def is_not_complex(a):
    if isinstance(a, complex):
        return False
    else:
        return True

counter = 1
if __name__ == "__main__":
    reader = FigureReader2("input.txt")
    figures = reader.read()
    maxAtributes = [figures[1].area(), figures[1].perimeter()]
    maxFigure = figures[0]
    for figure in figures:
        try:
            if is_not_complex(figure.area()) and is_not_complex(figure.perimeter()) and figure.area() > maxAtributes[0] and figure.perimeter() > maxAtributes[1] and isinstance(figure.area(), complex) == False :
                maxAtributes = [figure.area(), figure.perimeter()]
                maxFigure = figure
        except (AttributeError, TypeError):
            continue
    print("And the champion is ", maxFigure, "it's area =", {maxAtributes[0]}, "it's perimeter =", {maxAtributes[1]})