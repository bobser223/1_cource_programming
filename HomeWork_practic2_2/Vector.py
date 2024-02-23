

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
        turtle.goto(*list(map(float, self.vector)))
        turtle.setpos(*Vector.origin)
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
        max_comp = self.vector[0]

        for el in self.vector[1:]:
            if el > max_comp:
                max_comp = el
        return max_comp

    def min_comp(self):
        min_comp = self.vector[0]
        for el in self.vector[1:]:
            if el < min_comp:
                min_comp = el
        return min_comp

    def __str__(self) -> str:
        coordinates = list(map(float, self.vector))
        return f"Hi, I'm a Vector with coordinates: {coordinates}"

