class Person(object):
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'name: {self.name}, last name: {self.last_name},age: {str(self.age)}'

if __name__ == '__main__':
    p = Person('Volodymyr', 'Avvakumov', 18)
    print(p)
    print(p.name)
    print(p.last_name)
    print(p.age)