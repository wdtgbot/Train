import time

now = time.gmtime()
print(now)
hours = now[3]
print(hours)

import datetime

now = datetime.datetime.now()
time.sleep(3)
print(str(datetime.datetime.now() - now)[2:-7])
