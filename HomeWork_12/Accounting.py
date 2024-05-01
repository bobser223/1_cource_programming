class Accounting:

    def give_money(self, student, money: float, currency) -> None:  # Can be UAH/EUR/USD
        exchange_rate_dict = {"USD": 39.59, "EUR": 42.70, "UAH": 1}
        student.uah += money * exchange_rate_dict[currency]
        print("na hroshi")

    def __str__(self):
        return f"Accounting"

