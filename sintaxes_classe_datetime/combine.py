

"""
Objetivo:
    programar uma data final a partir de uma data inicial
"""

import datetime as dt
from datetime import datetime

# @datetime
print([1], now_time := datetime.now())
print([2], now_time_hour := now_time.hour)      # int(str(now_time).split()[1].split(':')[0])
print([3], now_time_minute := now_time.minute)  # int(str(now_time).split()[1].split(':')[1])
print([4], now_time_second := now_time.second)  # round(float(str(agora).split()[1].split(':')[2]))
print([5], month_length := dt.timedelta(days=31))
payment_date = dt.datetime.combine(
    now_time + month_length,
    dt.time(hour=now_time_hour, minute=now_time_minute, second=now_time_second)
)
print([6], payment_date)
