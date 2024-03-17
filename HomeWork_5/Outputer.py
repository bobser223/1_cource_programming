from Equation import Equation
from QuadraticEquation import QuadraticEquation
from BiQuadraticEquation import BiQuadraticEquation

class Outputer:
    def __init__(self, inputF):
        self.__inputF = inputF

    def fileReader(self):
        arguments = []
        with open(self.__inputF, "rt") as f:
            for line in f:
                argument = list(map(float, line.split()))
                arguments.append(argument)
            return arguments

    def initiator(self):
        arguments = self.fileReader()
        equations = []
        for argument in arguments:
            if len(argument) == 2:
                e = Equation(argument[0], argument[1])
                equations.append(e)
            elif len(argument) == 3:
                e = QuadraticEquation(argument[0], argument[1], argument[2])
                equations.append(e)
            else:  # len(argument) == 5
                e = BiQuadraticEquation(argument[0], argument[2], argument[4])
                equations.append(e)
        return equations

    def Solver(self):
        equations = self.initiator()
        answers = []
        for equation in equations:
            answers.append(equation.solve())
        return answers

    def find_equations(self, seqNum):
        equations = self.initiator()
        founded_equations = []
        for num in seqNum:
            founded_equations.append(equations[num])
        return founded_equations

    def EqWithNumberOfSol(self, numberOfSol):
        seqSolNumbs = []
        solutions = self.Solver()
        for i in range(len(solutions)):
            if len(solutions[i]) == numberOfSol and isinstance(solutions[i], tuple):
                seqSolNumbs.append(i)
        return self.find_equations(seqSolNumbs)

    def EqWithNoSol(self):
        return self.EqWithNumberOfSol(0)

    def EqWithOneSol(self):
        return self.EqWithNumberOfSol(1)

    def EqWithTwoSol(self):
        return self.EqWithNumberOfSol( 2)

    def EqWithThreeSol(self):
        return self.EqWithNumberOfSol(3)

    def EqWithFourSol(self):
        return self.EqWithNumberOfSol(4)

    def EqWithInfSol(self):
        seqSolNumbs = []
        solutions = self.Solver()
        for i in range(len(solutions)):
            if solutions[i] == BiQuadraticEquation.INF and isinstance(solutions[i], str):
                seqSolNumbs.append(i)
        return self.find_equations(seqSolNumbs)

    def minSol(self):
        eq = self.EqWithOneSol()
        minEl = eq[0].solve()[0]
        seqNum = 0
        for i in range(1, len(eq)):
            if eq[i].solve()[0] < minEl:
                minEl = eq[i].solve()[0]
                seqNum = i
        return eq[seqNum]

    def maxSol(self):
        eq = self.EqWithOneSol()
        maxEl = eq[0].solve()[0]
        seqNum = 0
        for i in range(1, len(eq)):
            if eq[i].solve()[0] > maxEl:
                maxEl = eq[i].solve()[0]
                seqNum = i
        return eq[seqNum]

    def output(self, outputFile):
        with open(outputFile, 'wt') as outF:
            with open(self.__inputF, 'r') as inpF:
                print(f"Data received from {self.__inputF}", file=outF)
                NoSol = self.EqWithNoSol()
                OneSol = self.EqWithOneSol()
                TwoSol = self.EqWithTwoSol()
                ThreeSol = self.EqWithThreeSol()
                FourSol = self.EqWithFourSol()
                InfSol = self.EqWithInfSol()
                print("polynomials without roots", file=outF)
                for eq in NoSol:
                    print(eq, file=outF)
                print("polynomials with the one root", file=outF)
                for eq in OneSol:
                    print(eq, file=outF)
                print("polynomials with two roots", file=outF)
                for eq in TwoSol:
                    print(eq, file=outF)
                print("polynomials with three roots", file=outF)
                for eq in ThreeSol:
                    print(eq, file=outF)
                print("polynomials with four roots", file=outF)
                for eq in FourSol:
                    print(eq, file=outF)
                print("polynomials with Infinum of roots", file=outF)
                for eq in InfSol:
                    print(eq, file=outF)
                print("polynomials with a minimal root", file=outF)
                print(self.minSol(), file=outF)
                print("polynomials with a maximal root", file=outF)
                print(self.maxSol(), file=outF)

if __name__ == "__main__":
    eqs1 = Outputer("input01.txt")
    eqs2 = Outputer("input02.txt")
    eqs3 = Outputer("input03.txt")
    eqs1.output("out01.txt")
    eqs2.output("out02.txt")
    eqs3.output("out3.txt")