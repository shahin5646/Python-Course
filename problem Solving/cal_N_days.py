""" How to Calculate number of days between two dates in Python """

from datetime import date

first_date = date(2024,6,14)
last_date = date(2000,12,19)

calculate = first_date - last_date
print(calculate.days)