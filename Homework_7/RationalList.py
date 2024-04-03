from Numbers import R

class RationalList:
    def __init__(self):
        self.list = []

    def __getitem__(self, index):
        return self.list[index]

    def __setitem__(self, index, item):
        assert type(index) == R
        self.list[index] = item

    def __len__(self):
        return len(self.list)

    def sum(self):
        suma = self.list[0]
        for i in range(1, len(self.list)):
            suma = suma + self.list[i]
        return suma

    def __add__(self, other):
        if isinstance(other, RationalList):
            new_list = RationalList()
            for item in self.list:
                new_list.list.append(item)
            for item in other:
                new_list.list.append(item)
            return new_list
        elif isinstance(other, int):
            new_list = RationalList()
            for item in self.list:
                new_list.list.append(item)
            new_list.list.append(R.set_by_sting(str(other)))
            return new_list
        elif isinstance(other, R):
            new_list = RationalList()
            for item in self.list:
                new_list.list.append(item)
            new_list.list.append(other)

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for item in other:
                self.list.append(item)

        elif isinstance(other, int):
            self.list.append(R(other))

        elif isinstance(other, R):
            self.list.append(other)

        return self



    def __str__(self):
        return str(self.list)

if __name__ == '__main__':
    r1 = R(7, 3)
    r2 = R(7, 8)
    r3 = R(7)
    rlst = RationalList()
    rlst.list = [1, 2, 3, 4, 5]
    rlst += r1
    rlst += r2
    rlst += r3
    l2 = RationalList()
    l2.list = [1, 2, 3, 4, 5]
    l3 = RationalList()
    l3.list = [1, 2, 3, 4, 5]
    print(l2 + l3)
    l2 += l3
    print(l2)
    rlst += 3
    print(rlst)


