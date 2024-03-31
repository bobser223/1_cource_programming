class Waiter:
    def __init__(self, name):
        self.name = name
        self.a = 0
        self.b = 1
    def serve(self):
        print(f"Waiter {self.name} serves ...")

class Singer:
    def __init__(self, name):
        self.name = name
        self.a = "Singer: p"
        self.b = "Singer:  o"

    def sing(self):
        print(f"Singer {self.name} sings ...")

# class SingerWaiter(Singer, Waiter):
#     def __init__(self, name):
#         Singer.__init__(self, name)
#         Waiter.__init__(self, name)

class SingerWaiter():
    def __init__(self, name):
        self.singer = Singer(name)
        self.waiter = Waiter(name)

if __name__ == "__main__":
    sw = SingerWaiter("Nikolya")
    # sw.sing()
    # sw.serve()
    print(sw.singer.a)
    print(sw.singer.b)
    print(sw.waiter.a)
    print(sw.waiter.b)