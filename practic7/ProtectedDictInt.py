class ProtectedDictInt:
    def __init__(self):
        self.__dict = {}

    def __setitem__(self, key, value):
        assert type(key) == int, "key must be integer"
        assert key not in self, "key cannot be reused" # if NO __contains__ use assert key not in self.__dict
        self.__dict[key] = value

    def __str__(self):
        return f"ProtectedDictInt: {self.__dict}"

    def __getitem__(self, key):
        return self.__dict[key]

    def __contains__(self, key):
        return key in self.__dict

    def __len__(self):
        return len(self.__dict)

    def __add__(self, other):
        # if type(other) == ProtectedDictInt:
        #     return ProtectedDictInt(**self, **other)
        if type(other) == ProtectedDictInt:
            new_d = ProtectedDictInt()
            for key, value in self.__dict.items():
                new_d.__setitem__(key, value)

            for key, value in other.__dict.items():
                new_d.__setitem__(key, value)
            return new_d
        elif type(other) == dict:
            new_d = ProtectedDictInt()
            for key, value in self.__dict.items():
                new_d.__setitem__(key, value)

            for key, value in other.items():
                new_d.__setitem__(key, value)
            return new_d

            # return ProtectedDictInt(**self, **other)
        elif type(other) == tuple:
            assert len(other) % 2 == 0
            new_d = ProtectedDictInt()
            for key, value in self.__dict.items():
                new_d.__setitem__(key, value)
            for i in range(0, len(other), 2):
                new_d.__setitem__(other[i], other[i+1])
            # new_d.__setitem__(other[0], other[1])
            return new_d

    def __sub__(self, key):
        new_d = self.__dict.copy()
        new_d.__delitem__(key)
        return new_d


    def __delitem__(self, key):
        del self.__dict[key]




if __name__ == '__main__':
    d = ProtectedDictInt()
    d[1] = -1
    d[2] = -2
    d[3] = -3
    d2 = ProtectedDictInt()
    d2[4] = -4
    d2[5] = -5
    d2[6] = -6
    print(d + d2)
    print(d - 3)
    print(d + (10, -10))
    print(d + {10: -10})