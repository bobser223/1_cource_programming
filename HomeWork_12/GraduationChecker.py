from StudentLifeSimulator import StudentLifeSimulator


class GraduationChecker(StudentLifeSimulator):
    def __init__(self, file_name):
        super().__init__(file_name)

    def check_graduation(self):
        student = self.life_imitation()
        if student.credits_required > 0:
            print(f"Student [{student}] has {student.credits_required} credits required, so he will not graduate")
        elif student.credits_required == 0:
            print(f"Student [{student}] will graduate")
        elif student.credits_required < 0:
            print(f"Student [{student}] studied {-student.credits_required} credits more so he will graduate")

if __name__ == "__main__":
    gr_ch = GraduationChecker("input01.txt")
    gr_ch.check_graduation()
    gr_ch = GraduationChecker("input02.txt")
    gr_ch.check_graduation()