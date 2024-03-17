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




def find_equations(filename, seqNum):
    equations = initiator(filename)
    founded_equations = []
    for num in seqNum:
        founded_equations.append(equations[num])
    return founded_equations


def EqWithNumberOfSol(filename, numberOfSol):
    seqSolNumbs = []
    solutions = Solver(filename)
    for i in range(len(solutions)):
        if len(solutions[i]) == numberOfSol and isinstance(solutions[i], tuple):
            seqSolNumbs.append(i)
    return find_equations(filename, seqSolNumbs)

def EqWithNoSol(filename):
    return EqWithNumberOfSol(filename, 0)

def EqWithOneSol(filename, string=True):
    return EqWithNumberOfSol(filename, 1)

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
    eq = EqWithOneSol(filename)
    minEl = eq[0].solve()[0]
    seqNum = 0
    for i in range(1, len(eq)):
        if eq[i].solve()[0] < minEl:
            minEl = eq[i].solve()[0]
            seqNum = i
    return eq[seqNum]

def maxSol(filename):
    eq = EqWithOneSol(filename)
    maxEl = eq[0].solve()[0]
    seqNum = 0
    for i in range(1, len(eq)):
        if eq[i].solve()[0] > maxEl:
            maxEl = eq[i].solve()[0]
            seqNum = i
    return eq[seqNum]




def output(inputFile, outputFile):
    with open(outputFile, 'wt') as outF:
        with open(inputFile, 'r') as inpF:
            print(f"Данні отримані з {outputFile}", file=outF)
            NoSol = EqWithNoSol(inputFile)
            OneSol = EqWithOneSol(inputFile)
            TwoSol = EqWithTwoSol(inputFile)
            ThreeSol = EqWithThreeSol(inputFile)
            FourSol = EqWithFourSol(inputFile)
            InfSol = EqWithInfSol(inputFile)
            print("многочлени без коренів", file=outF)
            for eq in NoSol:
                print(eq, file=outF)
            print("многочлени з 1-м коренем", file=outF)
            for eq in OneSol:
                print(eq, file=outF)
            print("многочлени з 2-ма коренями", file=outF)
            for eq in TwoSol:
                print(eq, file=outF)
            print("многочлени з 3-ма коренями", file=outF)
            for eq in ThreeSol:
                print(eq, file=outF)
            print("многочлени з 4-ма коренями", file=outF)
            for eq in FourSol:
                print(eq, file=outF)
            print("многочлени з безліччю коренів", file=outF)
            for eq in InfSol:
                print(eq, file=outF)
            print("многочлени з мінімальним коренем", file=outF)
            print(minSol(inputFile), file=outF)
            print("многочлени з максимальним коренем", file=outF)
            print(maxSol(inputFile), file=outF)


if __name__ == "__main__":
    output("input01.txt", "output01.txt")
    output("input02.txt", "output02.txt")
    output("input03.txt", "output03.txt")
    # print(Solver("input01.txt"))
    # print(EqWithNoSol("input01.txt"))
    # print(EqWithOneSol("input01.txt"))
    # print(EqWithTwoSol("input01.txt"))
    # print(EqWithThreeSol("input01.txt"))
    # print(EqWithFourSol("input01.txt"))
    # print(EqWithInfSol("input01.txt"))
    # print(maxSol("input01.txt"))
    # print(minSol("input01.txt"))
