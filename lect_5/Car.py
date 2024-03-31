class Car:
    def __init__(self):
        self.make = 'Volvo'
        self.model = "Cx-90"
        self.wheel = "18"
        self.engine = "245"

    def describe_car(self):
        print("Car", self.make, self.model, self.wheel, self.engine)


class LuxuryCar(Car):
    def __init__(self):
        super().__init__()
        self.audio = "JBL"
        self.seats = "Leather"
        self.color = "Crimson"
    # def __init__(self):
    #     self.audio = "JBL"
    #     self.seats = "Leather"
    #     self.color = "Crimson"

    def describe_car(self):
        print("Car", self.make, self.model, self.wheel, self.engine)
        print("Luxury", self.audio, self.seats, self.color)
if __name__ == "__main__":
    car = Car()
    car.describe_car()
    luxury = LuxuryCar()
    luxury.describe_car()