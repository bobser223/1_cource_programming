from Figure import Figure
from Triangle import Triangle
from Rectangle import Rectangle
from Rectangle import Rectangle
from Circle import Circle

class Car(Figure):

    def __init__(self):
        super().__init__()
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def draw(self):
        for component in self.components:
            component.position += self.position
        for component in self.components:
            component.draw()



if __name__ == '__main__':
    body = Rectangle(200, 100)
    window = Triangle(100, 0, 50, 100)
    window.set_position(50, 100)
    wheel1 = Circle(20)
    wheel2 = Circle(20)
    body.draw()
    window.draw()
    wheel1.set_position(35, -35)
    wheel2.set_position(165, -35)
    wheel1.draw()
    wheel2.draw()

    car = Car()
    car.add_component(body)
    car.add_component(window)
    car.add_component(wheel1)
    car.add_component(wheel2)
