class Quad:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminantum(self):
        return self.b**2 - 4*self.a*self.c

    def solution(self):
        solutions_list = []
        if self.a != 0:
            if self.discriminantum() < 0:
                return solutions_list
            if self.discriminantum() == 0:
                solutions_list.append(((-self.b) + self.discriminantum() ** 0.5) / (2*self.a))
                return solutions_list
            if self.discriminantum() > 0:
                solutions_list.append(((-self.b) + self.discriminantum() ** 0.5) / (2*self.a))
                solutions_list.append(((-self.b) - self.discriminantum() ** 0.5) / (2*self.a))
                solutions_list.sort()
                return solutions_list
        else:
            if self.b != 0:
                solutions_list.append((-self.c) / self.b)
                return solutions_list
            if self.b == 0:
                if self.c != 0:
                    return solutions_list
                else:
                    solutions_list.append("infinum")
                    return solutions_list

##########
if __name__ == "__main__":
    eq = Quad(0, 0, 4)
    print(eq.a, eq.b, eq.c)
    print(eq.discriminantum())
    print(eq.solution())