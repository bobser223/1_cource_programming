class Wheel:
    def isInflated(self):
        return True


class Engine:
    def run(self):
        print("Engine is running")



class Driver:
    def __init__(self, name):
        self._name = name
        self._car = car


    def drive(self):
        print(f"Driver {self._name} is driving")


class Car:

    def __init__(self, wheel):
        self._engine = Engine()  # композиція
        self._wheel = wheel  # агрегація
        self._driver = None # спочатку водія не вбудовують, тому це асоціація

    def set_driver(self, driver):
        self._driver = driver

    def drive(self, driver: Driver):
        if self._whell.isInflated():
            self._engine.run()
            driver.drive()

if __name__ == "__main__":
    wheel = Wheel()
    car = Car(wheel)

    driver = Driver("Bob")
    car.set_driver(driver)

