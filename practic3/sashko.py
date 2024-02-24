class Vector:
    def init(self, listOfCoordinates):

        self.listOfCoordinates = listOfCoordinates

    def size(self):
        return len(self.listOfCoordinates)

    def module(self):
        v = 0
        for i in self.listOfCoordinates:
            v += i**2
        return v**0.5

    def avarage(self):
        r = 0
        for i in self.listOfCoordinates:
            r = r+i
        return r / size(self.listOfCoordinates)

    def maximum(self):
        return max(vector)

    def minimumm(self):
        return min(vector)
