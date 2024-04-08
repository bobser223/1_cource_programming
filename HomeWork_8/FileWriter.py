from ConvertDataToRationalList import ConvertDataToRationalList
class FileWriter:
    def __init__(self, input_files, output_file):
        self.input_files = input_files
        self.output_file = output_file

    def write_output_data(self):
        with open(self.output_file, 'w') as output_file:
            for input_file in self.input_files:
                counter = 1
                converter = ConvertDataToRationalList(input_file)
                rational_lists = converter.convert()
                print(f"The file is {input_file}", file=output_file)
                for rational_list in rational_lists:
                    print(f"The rational_list is number  {counter}", file=output_file)
                    counter += 1
                    for rational_number in rational_list:
                        print(rational_number, file=output_file)