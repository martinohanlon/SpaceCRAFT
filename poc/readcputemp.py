import os
from time import time


t = open("/sys/class/thermal/thermal_zone0/temp", "r")
try:
    while True:
        starttime = time()
        t.seek(0)
        temp = t.readline()
        endtime = time()
        print(temp)
        print(endtime- starttime)
finally:
    t.close()
