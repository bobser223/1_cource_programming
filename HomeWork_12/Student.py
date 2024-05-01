from abc import ABCMeta, abstractmethod


class Student(metaclass=ABCMeta):
    def __init__(self, name,  credits_required, uah):
        self.name = name
        self.credits_required = credits_required
        self.uah = uah  # Ukrainian money
        self.humanities_count = 0
        self.natural_count = 0

    @abstractmethod
    def teach_humanitarian(self, credits: int) -> None:
        self.credits_required -= credits
        self.humanities_count += 1

    @abstractmethod
    def teach_natural(self, credits: int) -> None:
        self.credits_required -= credits
        self.natural_count += 1

    def get_scholarship(self, uah: float) -> None:
        self.uah += uah

    def rob_ancestors(self, uah: float) -> None:  # Money from parents
        self.uah += uah

    def pay_dormitory(self, uah: float) -> None:  # Money for home
        self.uah -= uah

    def pay_canteen(self, uah: float) -> None:  # Money for food
        self.uah -= uah