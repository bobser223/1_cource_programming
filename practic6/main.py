from Triangle import Triangle
from Rectangle import Rectangle
from Rectangle import Rectangle
from Circle import Circle

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