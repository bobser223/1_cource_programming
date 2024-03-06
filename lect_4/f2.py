class Wheel:
    def isInflated(self):
        return True


class Engine:
    def run(self):
        print("Engine is running")



class Driver:
    def __init__(self, name):
        self._name = name


    def drive(self):
        print(f"Driver {self._name} is driving")


class Car:

    def __init__(self, wheel):
        self._engine = Engine()  # композиція
        self._wheel = wheel  # агрегація
        self._drivers = [] # список водіїв


    def add_driver(self, driver):
        self._drivers.append(driver)

    def drive(self, driver_number):
        if self._wheel.isInflated() and driver_number < len(self._drivers):
            self._engine.run()
            driver = self._drivers[driver_number]
            driver.drive()

if __name__ == "__main__":
    wheel = Wheel()
    car = Car(wheel)

    driver = Driver("Bob")
    dr2 = Driver("Alice")

    car.add_driver(driver)
    car.add_driver(dr2)

    car.drive(1)