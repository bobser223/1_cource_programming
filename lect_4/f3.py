class Animal:

    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"Тварина {self.name} рухається")


class Dog(Animal):

    def speak(self):
        print(f"Собака {self.name} гавкає")



class Cat(Animal):
    def speak(self):
        print(f"Кіт {self.name} мявкає")

class Lizard(Animal):

    def speak(self):
        print(f"Ящірка {self.name} шипить")


if __name__ == "__main__":
     dog = Dog("Barbos")
     dog.move()
     dog.speak()

     cat = Cat("Robert")
     cat.speak()
     cat.move()

     lizard = Lizard("Артемій")
     dog.move()
     dog.speak()
