from FileReader import FileReader
from R import R
from RationalList import RationalList
from ConvertDataToRationalList import ConvertDataToRationalList

if __name__ == "__main__":
    for file in ("inp01.txt", "inp02.txt", "inp03.txt"):
        counter = 1
        converter = ConvertDataToRationalList(file)
        rational_lists = converter.convert()
        print(f"The file is {file}")
        for rational_list in rational_lists:
            print(f"The rational_list is number  {counter}")
            counter += 1
            for rational_number in rational_list:
                print(rational_number)
