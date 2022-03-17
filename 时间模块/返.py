import time

ksrq = "2022-03-17"

if time.strptime(ksrq, "%Y-%m-%d") < time.gmtime():
    print("11111")
else:
    print("00000")
    