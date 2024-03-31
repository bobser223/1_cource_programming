class ProtectedDictInt(dict):
    def __setitem__(self, key, value):
        assert type(key) == int, "key must be integer"
        assert key not in self, "key cannot be reused"
        super().__setitem__(key, value)
        # self[key] = value can't do in or we will have recursion


if __name__ == '__main__':
    d = ProtectedDictInt()
    d[234] = "world"
    # d["pipiska"] = 123
    print(234 in d)
    print(445 in d)
    print(d)
    d.update({"hello": "world"})
    print(d)