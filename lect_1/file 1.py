class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 0
        pass

    def growUp(self):
        self.age += 1

    def bite(self, other):
        print(f"Cat'{self.name}'bites '{other.name}'")
    def miu(self):
        print(f"Cat '{self.name}' says: Miu")



catVasya = Cat("Vasya")
catKuzia = Cat("Kuzia")
catBob = Cat("Bob")

catVasya.miu()
catKuzia.miu()
print(catVasya.name)
print(catKuzia.name)
catVasya.growUp()
print(catVasya.age)
catKuzia.bite(catVasya)