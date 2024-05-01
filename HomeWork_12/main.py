from HumanitarianStudent import HumanitarianStudent
from NaturalStudent import NaturalStudent
from HumNatStudent import HumNatStudent
from HumanitarianTeacher import HumanitarianTeacher
from NaturalTeacher import NaturalTeacher

if __name__ == '__main__':
    hum_student = HumanitarianStudent("Vasia", 33, 230)
    nat_student = NaturalStudent("minion", 2, 44)
    hum_teacher = HumanitarianTeacher("Alfred")
    print(hum_student)
    hum_student.teach_humanitarian(hum_teacher, 3)
    print(hum_student)
