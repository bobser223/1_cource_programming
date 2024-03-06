class Foo:
    def __init__(self):
        self._bar = "pipka (bar)"
        self.__baz = "pipka (baz)"



    def __str__(self):
        return "Foo: bar" + self._bar + "baz:" + self.__baz


if __name__ == "__main__":
    foo = Foo()
    print(foo)
    foo._bar = "pipka2 (bar)"
    foo._Foo__baz = "New baz"
    print(foo)
    # foo.__baz = "pipka3 (baz)"
    # print(foo.__baz)

    print(foo)
