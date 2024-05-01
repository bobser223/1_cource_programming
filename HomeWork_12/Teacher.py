from abc import ABCMeta, abstractmethod


class Teacher(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def teach_natural(self):
        pass

    @abstractmethod
    def teach_humanitarian(self):
        pass

