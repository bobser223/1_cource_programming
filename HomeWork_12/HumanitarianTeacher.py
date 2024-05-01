from Teacher import Teacher
from NaturalStudent import NaturalStudent

class HumanitarianTeacher(Teacher):
    def __init__(self, name, fortran_pension=None):
        super().__init__(name)
        self.fortran_pension = fortran_pension

    def teach_natural(self, student, credit):
        if isinstance(student, NaturalStudent):
            raise AssertionError("The dean's office messed up again, I'm humanitarian teacher,"
             " not natural (no connection with steroids)")
        student.credits_required -= credit

        student.natural_count += 1

    def teach_humanitarian(self, student, credit):
        if isinstance(student, NaturalStudent):
            raise AssertionError("The dean's office messed up again, I'm humanitarian teacher,"
                                 " not natural (no connection with steroids)")
        student.credits_required -= credit
        student.humanities_count += 1



    def __str__(self):
        return f"Humanitarian teacher: {self.name}"
