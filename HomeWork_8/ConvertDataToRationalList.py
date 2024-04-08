from FileReader import FileReader
from R import R
from RationalList import RationalList
# from FileWriter import FileWriter

class ConvertDataToRationalList(FileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def convert(self):
        list_of_rational_lists = []
        list_of_lines = self.read_file()
        for line in list_of_lines:
            r_lst = RationalList()
            for el in line:
                r_lst += R(el)
            list_of_rational_lists.append(r_lst)

        return list_of_rational_lists

