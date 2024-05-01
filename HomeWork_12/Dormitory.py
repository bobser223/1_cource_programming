class Dormitory:
    def __str__(self):
        return "Dormitory"

    def take_money(self, student, money: float, currency) -> None:  # Can be UAH/EUR/USD
        exchange_rate_dict = {"USD": 39.59, "EUR": 42.70, "UAH": 1}
        uah = exchange_rate_dict[currency] * money
        if student.uah <= 0 or student.uah < uah:
            raise Exception("Not enough money, go to the work, no more university 4 u!!!!!!!!")
        student.uah -= uah
        print("syda 'Dormitory'")

