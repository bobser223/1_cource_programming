from Teacher import Teacher


class NaturalTeacher(Teacher):
    def __init__(self, name, fortran_pension=None):
        super().__init__(name)
        self.fortran_pension = fortran_pension

    def teach_natural(self, student, credit):
        student.credits_required -= credit

        student.natural_count += 1

    def teach_humanitarian(self, student, credit):
        raise TypeError("The dean's office messed up again, I'm natural teacher, not humanitarian")

    def teach_humanitarian_and_natural(self, student, credit, subject_type):
        student.credits_required -= credit
        if subject_type == "natural":
            student.natural_count += 1
        else:  # Subject_type == "humanitarian"
            student.humanitarian_count += 1

    def __str__(self):
        return f"Natural teacher: {self.name}"