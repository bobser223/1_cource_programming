class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        list_of_lines = []
        with open(self.filename, "rt") as f:
            for line in f:
                list_of_lines.append(line.split())
        return list_of_lines
