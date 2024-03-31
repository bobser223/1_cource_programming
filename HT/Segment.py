class Segment:
    def __init__(self, start, end, start_point, end_point):
        self.start = start
        self.end = end
        self.start_point = start_point
        self.end_point = end_point

    def is_empty(self):
        if self.start < self.end or (self.start == self.end and (self.start_point == False or  self.end_point == False)) :
            return True
        return False

    @staticmethod
    def anti_Lambda(a):
        if a:
            return "["
        else:
            return "("
    @staticmethod
    def anti_Lambda2(a):
        if a:
            return "]"
        else:
            return ")"

    def __add__(self, other):
        if self.start <= other.end or other.start <= self.end:

            min_start = min(self.start, other.start)
            max_end = max(self.end, other.end)
            if self.start == other.start:
                if self.start_point == True or other.start_point == True:
                    new_start_point = True
                else:
                    new_start_point = False
            elif self.start == min_start:
                new_start_point = self.start_point
            elif other.start == min_start:
                new_start_point = other.start_point
            ########
            if self.end == other.end:
                if self.end_point == True or other.end_point == True:
                    new_end_point = True
                else:
                    new_end_point = False
            elif self.end == max_end:
                new_end_point = self.end_point
            elif other.end == max_end:
                new_end_point = other.end_point

            ####
            return Segment(min_start, max_end, new_start_point, new_end_point)

    def __mul__(self, other):
        if self.start < other.end:
            new_start = self.start
            new_end = other.end

        elif other.start < self.end:
            new_start = other.start
            new_end = other.end
        return Segment(new_start, new_end)

        if
    def __str__(self):
        return f"{self.anti_Lambda(self.start_point)} {self.start}, {self.end} {self.anti_Lambda2(self)}"




if __name__ == "__main__":
    segment = Segment(1, 3, False, True) # (2, 3]
    print(segment)
    segment2 = Segment(2, 5, True, False)
    print(segment2)
    print(segment + segment2)

