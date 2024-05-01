from FileReader import FileReader


class ActivityTracker(FileReader):
    def __init__(self, file_name):
        super().__init__(file_name)

    def find_out_activity(self):
        life_list = []
        data = self.read_file()

        for _ in range(3):
            life_list.append(data[0][0])
            data.pop(0)

        for line in data:
            if line[0] == 'teach':
                if line[1] == "humanitarian":
                    life_list.append(['teach_humanitarian', int(line[2])])
                elif line[1] == 'natural':
                    life_list.append(['teach_natural', int(line[2])])
            elif line[0] == 'obtain':
                life_list.append(["get_scholarship", int(line[2])])
            elif line[0] == 'pay':
                if line[1] == "canteen":
                    life_list.append(["pay_canteen", int(line[2])])
                elif line[1] == 'hostel':
                    life_list.append(["pay_dormitory", int(line[2])])
        return life_list



if __name__ == '__main__':
    tracker = ActivityTracker('input01.txt')
    print(tracker.find_out_activity())

