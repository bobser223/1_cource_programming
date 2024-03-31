from File_solver import File_solver

if __name__ == "__main__":
    file1 = File_solver("input01.txt")
    # print(file1.solver())
    for answer in file1.solver():
        print(answer)
