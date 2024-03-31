class Waiter:
    def __init__(self, name):
        self.name = name

    def serve(self):
        print(f"Waiter {self.name} serves ...")

class Singer:
    def __init__(self, name):
        self.name = name

    def sing(self):
        print(f"Singer {self.name} sings ...")

class SingerWaiter(Singer, Waiter):
    def __init__(self, name):
        

if __name__ == "__main__":
    sw = SingerWaiter("Nikolya")
    sw.sing()
    sw.serve()