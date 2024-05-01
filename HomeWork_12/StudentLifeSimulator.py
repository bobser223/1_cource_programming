from ActivityTracker import ActivityTracker
# students/teachers
from HumanitarianStudent import HumanitarianStudent
from NaturalStudent import NaturalStudent
from HumNatStudent import HumNatStudent
from HumanitarianTeacher import HumanitarianTeacher
from NaturalTeacher import NaturalTeacher
# institutions
from Accounting import Accounting
from Canteen import Canteen
from Dormitory import Dormitory


class StudentLifeSimulator(ActivityTracker):
    def __init__(self, file_name):
        super().__init__(file_name)

    def init_student(self):
        student_dict = {'humanitarian': HumanitarianStudent, 'natural': NaturalStudent, "natural-humanitarian": HumNatStudent}
        life_activities = self.find_out_activity()
        student = student_dict[life_activities[0]]("HentaiLover", int(life_activities[1]), int(life_activities[2]))
        return student

    @staticmethod
    def teacher_chooser(student):
        if isinstance(student, HumanitarianStudent):
            teacher = HumanitarianTeacher("HentaiLover")
            return teacher
        teacher = NaturalTeacher("ComputerLover")
        return teacher

    @staticmethod
    def make_institutions_dict() -> dict:
        canteen = Canteen()
        dormitory = Dormitory()
        accounting = Accounting()
        institutions_dict = {"get_scholarship": accounting, "pay_canteen": canteen, "pay_dormitory": dormitory}
        return institutions_dict

    def life_imitation(self):
        student = self.init_student()
        teacher = self.teacher_chooser(student)
        activities_dict = {"teach_humanitarian": student.teach_humanitarian, "teach_natural": student.teach_natural,
                           "get_scholarship": student.get_scholarship, "pay_canteen": student.pay_canteen,
                           "pay_dormitory": student.pay_dormitory}

        institutions_dict = self.make_institutions_dict()
        life_activities = self.find_out_activity()
        for i in range(3, len(life_activities)):
            if life_activities[i][0] == "teach_humanitarian":
                activities_dict["teach_humanitarian"](teacher, life_activities[i][1])
            elif life_activities[i][0] == "teach_natural":
                activities_dict["teach_natural"](teacher, life_activities[i][1])
            else:
                activities_dict[life_activities[i][0]](institutions_dict[life_activities[i][0]], life_activities[i][1])
                # student.action(Visitor, money)
        return student


if __name__ == '__main__':
    sim = StudentLifeSimulator('input01.txt')
    print(sim.init_student())
    print(sim.life_imitation())

    sim = StudentLifeSimulator('input02.txt')
    print(sim.init_student())
    print(sim.life_imitation())



