# /usr/bin/env python
# -*- coding=utf-8 -*-

from time import sleep
from os import system

while True:
    with open("./a.txt", "r", encoding="utf-8") as f1:
        t1 = f1.read()
    sleep(2)
    with open("./a.txt", "r", encoding="utf-8") as f2:
        t2 = f2.read()
    if t1 != t2:
        system("crontab /data/crontab.sh")
