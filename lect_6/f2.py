class Copier:
    def copy(self):
        print("Copier is coping")



class Xerox(Copier):
    pass
    # def copy(self):
    #     print("Xerox is coping")



class Scaner:
    def copy(self):
        print("Scaner is coping")


class MFD(Xerox, Scaner):
    # def copy(self):
    #     print("MFD is coping")
    pass



if __name__ == "__main__":
    xerox = Xerox()
    scaner = Scaner()
    xerox.copy()
    scaner.copy()
    mfd = MFD()
    mfd.copy()
    print(MFD.__mro__)

