import datetime

current_time = datetime.datetime.now()

year = current_time.year
month = current_time.month
day = current_time.day
hour = current_time.hour
minute = current_time.minute
second = current_time.second
microsecond = current_time.microsecond

print("Рік:", year)
print("Місяць:", month)
print("День:", day)
print("Година:", hour)
print("Хвилина:", minute)
print("Секунда:", second)
print("Мікросекунда:", microsecond)
