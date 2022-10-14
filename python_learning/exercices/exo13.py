import datetime
from datetime import date
import random


start_date = date.today().replace(day=1, month=1).toordinal()
end_date = date.today().replace(day=31, month=12).toordinal()
random_day = date.fromordinal(random.randint(start_date, end_date))
random_day = datetime.datetime(random_day.year, random_day.month, random_day.day)


print(random_day)

print(datetime.datetime.now() - random_day)