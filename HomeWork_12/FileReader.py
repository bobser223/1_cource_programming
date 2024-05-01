class FileReader:
    def __init__(self, file: str):
        self.file = file

    def read_file(self) -> list:
        content = []
        with open(self.file) as f:
            for line in f:
                content.append(line.split())
        return content


if __name__ == "__main__":
    file_reader = FileReader("input01.txt")
    print(file_reader.read_file())