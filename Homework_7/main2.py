from Numbers import R
from RationalList import RationalList


def reader(file):
    lines = []
    with open(file, "rt") as f:
        for line in f:
            lines.append(line.split())
        return lines

def changer(file):
    lines = reader(file)
    rational_lists = []
    for line in lines:
        r_lst = RationalList()
        for el in line:
            r_lst += R.set_by_sting(el)
        rational_lists.append(r_lst)
    return rational_lists

def calculate(r_lst):
    suma = r_lst[0]
    for i in range(1, len(r_lst)):
        suma = suma + r_lst[i]
    return suma

def file_calculate(file):
    answers = []
    rational_lists = changer(file)
    for rational_list in rational_lists:
        answers.append(calculate(rational_list))
    return answers

if __name__ == "__main__":
    for file in ("inp01.txt", "inp02.txt", "inp03.txt"):
        print(*file_calculate(file), sep="\n")

