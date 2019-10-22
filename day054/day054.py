# Day 54

import datetime

yesterday = datetime.date.today() - datetime.timedelta(days=1)
tomorrow = datetime.date.today() - datetime.timedelta(days=-1)

print(f"Yesterday was {yesterday}")
print(f"Tomorrow will be {tomorrow}")
