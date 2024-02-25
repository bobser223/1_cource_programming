import turtle

class Vector:
    origin = [0, 0]

    def __init__(self, vector=list):
        if isinstance(vector, Vector):
            self.vector = vector.vector
        else:
            assert len(vector) > 0
            self.vector = vector


    def draw(self):
        turtle.up()
        turtle.setpos(*Vector.origin)
        turtle.down()
        if len(self.vector) == 1:
            turtle.goto(self.vector[0])
        else:
            turtle.goto(self.vector[0], self.vector[1])
        # turtle.setpos(*Vector.origin)
        turtle.up()

    def dimension(self): #розмірність
        return len(self.vector)

    def length(self):  #довжина
        length = 0
        for number in self.vector:
            length += float(number) ** 2
        return length ** 0.5

    def mean(self):  # середнє арифметичне
        return sum(self.vector) / len(self.vector)

    def sum_vector(self):
        return sum(self.vector)

    def max_comp(self):
        # max_comp = self.vector[0]
        #
        # for el in self.vector[1:]:
        #     if el > max_comp:
        #         max_comp = el
        # return max_comp
        return max(self.vector)

    def min_comp(self):
        # min_comp = self.vector[0]
        # for el in self.vector[1:]:
        #     if el < min_comp:
        #         min_comp = el
        # return min_comp
        return min(self.vector)

    def __str__(self) -> str:
        coordinates = list(map(float, self.vector))
        return f"Hi, I'm a Vector with coordinates: {coordinates}"


if __name__ == "__main__":
    v1 = Vector([1000, 300, 15])
    v2 = v1
    # v2 = Vector(v1)
    # v2 = [12, 13]
    v2 = Vector([-300, 200, 3])
    turtle.speed(0)
    print(v1)
    print(v2)
    v2.draw()
    v1.draw()
    turtle.mainloop()