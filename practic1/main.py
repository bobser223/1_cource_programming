from f1 import Quad

def soluter(input_list):
    with open(input_list, "rt") as f:
        solution_list = []
        while True:
            try:
                str_of_coef = f.readline()
                list_of_coef = str_of_coef.split()
                list_of_coef = list(map(float, list_of_coef))
                a = list_of_coef[0]
                b = list_of_coef[1]
                c = list_of_coef[2]
                eq = Quad(a, b, c)
                solution_list.append(eq.solution())
            except IndexError:
                return solution_list






print(*soluter("input01.txt"))
print(*soluter("input02.txt"))
print(*soluter("input03.txt"))