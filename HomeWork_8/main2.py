from FileWriter import FileWriter

if __name__ == "__main__":
    fileWriter = FileWriter(("inp01.txt", "inp02.txt", "inp03.txt"), "output03.txt")
    fileWriter.write_output_data()
