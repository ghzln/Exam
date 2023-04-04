import random
import datetime
import collections

start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)
num_dates = 600
dates = [start_date + datetime.timedelta(days=random.randint(0, 365)) for _ in range(num_dates)]

month_counts = collections.Counter(date.month for date in dates)

for month in range(1, 13):
    count = month_counts[month]
    print(f"{datetime.date(2022, month, 1).strftime('%B')}: {count}")



    # a list of 600 random dates between january 1 2023 and december 31 2023 
    # finally the code print the months
