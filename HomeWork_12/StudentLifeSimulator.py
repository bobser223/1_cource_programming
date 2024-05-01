from ActivityTracker import ActivityTracker
from HumanitarianStudent import HumanitarianStudent
from NaturalStudent import NaturalStudent
from HumNatStudent import HumNatStudent
from HumanitarianTeacher import HumanitarianTeacher
from NaturalTeacher import NaturalTeacher


class StudentLifeSimulator(ActivityTracker):
    def __init__(self, file_name):
        super().__init__(file_name)

    def init_student(self):
        student_dict = {'humanitarian': HumanitarianStudent, 'natural': NaturalStudent, "natural-humanitarian": HumNatStudent}
        life_activities = self.find_out_activity()
        student = student_dict[life_activities[0]]("HentaiLover", int(life_activities[1]), int(life_activities[2]))
        return student

    def life_imitation(self):
        hum_teacher = HumanitarianTeacher("lox")
        nat_teacher = NaturalTeacher("NeLox")
        student = self.init_student()
        activities_dict = {"teach_humanitarian": student.teach_humanitarian, "teach_natural": student.teach_natural,
                           "get_scholarship": student.get_scholarship, "pay_canteen": student.pay_canteen,
                           "pay_dormitory": student.pay_dormitory}
        life_activities = self.find_out_activity()
        for i in range(3, len(life_activities)):
            if life_activities[i][0] == "teach_humanitarian":
                activities_dict["teach_humanitarian"](hum_teacher, life_activities[i][1])
            elif life_activities[i][0] == "teach_natural":
                activities_dict["teach_natural"](nat_teacher, life_activities[i][1])
            else:
                activities_dict[life_activities[i][0]](life_activities[i][1])
        return student


if __name__ == '__main__':
    sim = StudentLifeSimulator('input01.txt')
    print(sim.init_student())
    print(sim.life_imitation())

    sim = StudentLifeSimulator('input02.txt')
    print(sim.init_student())
    print(sim.life_imitation())



