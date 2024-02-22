from FigureReader2 import FigureReader2
def is_not_complex(a):
    if isinstance(a, complex):
        return False
    else:
        return True

def finalResult(a_file):
    reader = FigureReader2(a_file)
    figures = reader.read()
    maxAttributes = [0, 0]  # відповідно ні проща, ні периметер не можуть бути менші за 0
    maxFigure = figures[0]
    for figure in figures:
        try:
            if is_not_complex(figure.area()) and is_not_complex(lenthPerimeterSwitcher(figure)) and figure.area() > maxAttributes[0] and lenthPerimeterSwitcher(figure) > maxAttributes[1]:
                maxAttributes = [figure.area(), lenthPerimeterSwitcher(figure)]
                maxFigure = figure
        except (AttributeError, TypeError):
            continue

    print("And the champion is", maxFigure, "it's area =", maxAttributes[0],(lambda: "and it's length =" if maxFigure.__class__.__name__ == "Circle" else "and it's perimeter =")(),maxAttributes[1])

def lenthPerimeterSwitcher(a_figure):
    if a_figure.__class__.__name__ == "Circle":
        return a_figure.length()
    else:
        return a_figure.perimeter()







if __name__ == "__main__":
    for file in ["input01.txt", "input02.txt", "input03.txt"]:
        finalResult(file)



# if __name__ == "__main__":
#     for file in ["input01.txt", "input02.txt", "input03.txt"]:
#         reader = FigureReader2(file)
#         figures = reader.read()
#         maxAttributes = [0, 0] # відповідно ні проща, ні периметер не можуть бути менші за 0
#         maxFigure = figures[0]
#         for figure in figures:
#             try:
#                 if is_not_complex(figure.area()) and is_not_complex(lenthPerimeterSwitcher(figure)) and figure.area() > maxAttributes[0] and lenthPerimeterSwitcher(figure) > maxAttributes[1] and isinstance(figure.area(), complex) == False :
#                     maxAttributes = [figure.area(), lenthPerimeterSwitcher(figure)]
#                     maxFigure = figure
#             except (AttributeError, TypeError):
#                 continue
#         print("And the champion is", maxFigure, "it's area =", maxAttributes[0], (lambda: "and it's length =" if maxFigure.__class__.__name__ == "Circle"  else "and it's perimeter =")(), maxAttributes[1])

# def Kostyl_for_maxAtributes(a):
#     reader = FigureReader2("input01.txt")
#     figures = reader.read()
#     maxAtributes = [0,0]
#     for figure in figures:
#         try:
#             maxAtributes[0] = figure.area()
#             maxAtributes[1] = figure.perimeter()
#         except AttributeError:
#             continue
#     return maxAtributesgit add .
