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

    def get_scholarship(self, accounting, money: float, currency="UAH") -> None:  #UAH/EUR/USD possible
        accounting.give_money(self, money, currency)

    def rob_ancestors(self, uah: float) -> None:  # Money from parents
        self.uah += uah

    def pay_dormitory(self, dormitory, money: float, currency="UAH") -> None:  # UAH/EUR/USD possible
        dormitory.take_money(self, money, currency)  # Money fore flat

    def pay_canteen(self, canteen, money: float, currency="UAH") -> None:  # UAH/EUR/USD possible
        canteen.take_money(self, money, currency)  # Money fore food