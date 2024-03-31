class Popka:
    def __init__(self, hair):
        self.hair = True

    def poo(self):
        if self.hair:
            print("borebuh")
        print("NO borebuh")

class HH(Popka):
    def __init__(self, hair, pelmen):
        Popka.__init__(self, hair)
        self.pelmen = pelmen


h = HH(True, 2)
h.poo()
