from Teacher import Teacher
from HumanitarianStudent import HumanitarianStudent

class NaturalTeacher(Teacher):
    def __init__(self, name, fortran_pension=None):
        super().__init__(name)
        self.fortran_pension = fortran_pension

    def teach_natural(self, student, credit):
        if isinstance(student, HumanitarianStudent):
            raise AssertionError("The dean's office messed up again, I'm natural teacher, not humanitarian")
        student.credits_required -= credit

        student.natural_count += 1

    def teach_humanitarian(self, student, credit):
        if isinstance(student, HumanitarianStudent):
            raise AssertionError("The dean's office messed up again, I'm natural teacher, not humanitarian")
        student.credits_required -= credit

        student.humanities_count += 1

    def __str__(self):
        return f"Natural teacher: {self.name}"