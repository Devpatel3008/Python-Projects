from datetime import datetime
import pytz
import time
"""

home = pytz.timezone('Asia/Kolkata')
local_time = datetime.now(home)
current_date = local_time.date()
current_time=local_time.strftime("%H:%M:%S")
print(local_time)
print(current_time)
print(current_date)


"""
#For All TImezones stored in libraries
for tz in pytz.all_timezones:
	print(tz)
