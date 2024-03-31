class Animal:

    def __init__(self, name):
        self.name = name

    def get_animal_type(self):
        return "Animal"

    def move(self):
        print(f"Тварина {self.get_animal_type()} {self.name} рухається")


class Dog(Animal):


    def get_animal_type(self):
        return "Dog"

class Cat(Animal):


    def get_animal_type(self):
        return "Cat"

if __name__ == "__main__":
    dog = Dog("Barbos")
    dog.move()
    cat = Cat("Batman")
    cat.move()
    animal = Animal("Pipka")
    animal.move()



