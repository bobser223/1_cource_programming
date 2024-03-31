from Numbers import I
from Numbers import R

class File_solver:
    def __init__(self, file_name):
        self.f_name = file_name


    def file_reader(self):
        data = []
        with open(self.f_name, "rt") as f:
            for line in f:
                data.append(line.split())
        return data

    @staticmethod
    def R_reaplacer(lst):
        while True:
            for i in range(len(lst)):
                if "/" in lst[i] and type(lst[i]) != R:
                    for j in range(len(lst[i])):
                        if lst[i][j] == "/":
                            r = R(int(lst[i][0: j]), int(lst[i][j+1:]))
                            lst[i] = r
                            break
            else:
                break
        return lst

    @staticmethod
    def I_reaplacer(lst):
        while True:
            for i in range(len(lst)):
                if type(lst[i]) != R and "/" not in lst[i] and "*" not in lst[i] and "+" not in lst[i] and "-" not in lst[i]:
                    integer = I(int(lst[i]))
                    lst[i] = integer
            else:
                break
        return lst

    @staticmethod
    def mult_performer(lst):
        while True:
            for i in range(len(lst)):
                if lst[i] == "*":
                    lst[i] = lst[i - 1] * lst[i + 1]
                    lst.pop(i - 1)
                    lst.pop(i)
                    break
            else:
                break
        return lst

    @staticmethod
    def simp_arith_operations_performer(lst):
        while True:
            for i in range(len(lst)):
                if lst[i] == "-":
                    lst[i] = lst[i - 1] - lst[i + 1]
                    lst.pop(i - 1)
                    lst.pop(i)
                    break

                if lst[i] == "+":
                    lst[i] = lst[i - 1] + lst[i + 1]
                    lst.pop(i - 1)
                    lst.pop(i)
                    break

                if lst[i] == "-":
                    lst[i] = lst[i - 1] - lst[i + 1]
                    lst.pop(i - 1)
                    lst.pop(i)
                    break

            else:
                break
        answer = lst[0]
        return answer

    def solver(self):
        answers = []
        data = self.file_reader()
        for line in data:
            line_with_R = self.R_reaplacer(line)
            line_with_I_and_R = self.I_reaplacer(line_with_R)
            mult_line = self.mult_performer(line_with_I_and_R)
            final_result = self.simp_arith_operations_performer(mult_line)
            answers.append(final_result)
        return answers

