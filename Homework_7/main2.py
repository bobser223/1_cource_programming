from Numbers import R
from RationalList import RationalList


def read(file):
    lines = []
    with open(file, "rt") as f:
        for line in f:
            lines.append(line.split())
        return lines

def add_rationals_to_rational_list(file):
    lines = read(file)
    rational_lists = []
    for line in lines:
        r_lst = RationalList()
        for el in line:
            r_lst += R.set_by_sting(el)
        rational_lists.append(r_lst)
    return rational_lists

# def calculate(r_lst):
#     suma = r_lst[0]
#     for i in range(1, len(r_lst)):
#         suma = suma + r_lst[i]
#     return suma

#calculate(rational_list)

def calculate(file):
    answers = []
    rational_lists = add_rationals_to_rational_list(file)
    for rational_list in rational_lists:
        answers.append(rational_list.sum())
    return answers

if __name__ == "__main__":
    for file in ("inp01.txt", "inp02.txt", "inp03.txt"):
        print(f"answers to file {file}")
        print(*calculate(file), sep="\n")

