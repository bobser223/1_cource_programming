from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation



def fileReader(filename):
    arguments = []
    with open(filename, "rt") as f:
        for line in f:
            argument = list(map(float, line.split()))
            arguments.append(argument)
        return arguments

def initiator(filename):
    arguments = fileReader(filename)
    equations = []
    for argument in arguments:
        if len(argument) == 2:
            e = Equation(argument[0], argument[1])
            equations.append(e)
        elif len(argument) == 3:
            e = QuadraticEquation(argument[0], argument[1], argument[2])
            equations.append(e)
        else: # len(argument) == 5
            e = BiQuadraticEquation(argument[0], argument[2], argument[4])
            equations.append(e)
    return equations

def Solver(filename):
    equations = initiator(filename)
    answers = []
    for equation in equations:
        answers.append(equation.solve())
    return answers




def find_equations(filename, seqNum, string=True):
    equations = initiator(filename)
    founded_equations = []
    for num in seqNum:
        if string:
            founded_equations.append(equations[num].__str__())
        else:
            founded_equations.append(equations[num])
    return founded_equations


def EqWithNumberOfSol(filename, numberOfSol, string=True):
    seqSolNumbs = []
    solutions = Solver(filename)
    for i in range(len(solutions)):
        if len(solutions[i]) == numberOfSol and isinstance(solutions[i], tuple):
            seqSolNumbs.append(i)
    return find_equations(filename, seqSolNumbs, string)

def EqWithNoSol(filename):
    return EqWithNumberOfSol(filename, 0)

def EqWithOneSol(filename, string=True):
    return EqWithNumberOfSol(filename, 1, string)

def EqWithTwoSol(filename):
    return EqWithNumberOfSol(filename, 2)

def EqWithThreeSol(filename):
    return EqWithNumberOfSol(filename, 3)

def EqWithFourSol(filename):
    return EqWithNumberOfSol(filename, 4)

def EqWithInfSol(filename):
    seqSolNumbs = []
    solutions = Solver(filename)
    for i in range(len(solutions)):
        if solutions[i] == BiQuadraticEquation.INF and isinstance(solutions[i], str):
            seqSolNumbs.append(i)
    return find_equations(filename, seqSolNumbs)

def countOfFourElementsAnwers(answers):
    counter = 0
    for answer in answers:
        if len(answer) == 4:
            counter += 1
    return counter

def minSol(filename):
    eq = EqWithOneSol(filename, False)
    minEl = eq[0].solve()[0]
    seqNum = 0
    for i in range(1, len(eq)):
        if eq[i].solve()[0] < minEl:
            minEl = eq[i].solve()[0]
            seqNum = i
    return eq[seqNum]

def maxSol(filename):
    eq = EqWithOneSol(filename, False)
    maxEl = eq[0].solve()[0]
    seqNum = 0
    for i in range(1, len(eq)):
        if eq[i].solve()[0] > maxEl:
            maxEl = eq[i].solve()[0]
            seqNum = i
    return eq[seqNum]





if __name__ == "__main__":
    print(Solver("input01.txt"))
    print(EqWithNoSol("input01.txt"))
    print(EqWithOneSol("input01.txt"))
    print(EqWithTwoSol("input01.txt"))
    print(EqWithThreeSol("input01.txt"))
    print(EqWithFourSol("input01.txt"))
    print(EqWithInfSol("input01.txt"))
    print(maxSol("input01.txt"))
    print(minSol("input01.txt"))
