#read all astro pi sensors
#a test to see how quick it is

from time import time, sleep
from astro_pi import AstroPi

ap = AstroPi()
ap.get_humidity()
ap.get_pressure()
ap.get_orientation()

while(True):
    starttime = time()

    hum = ap.get_humidity()
    pres = ap.get_pressure()
    temp1 = ap.get_temperature_from_humidity()
    temp1 = ap.get_temperature_from_pressure()
    rads = ap.get_orientation_radians()
    degs = ap.get_orientation_degrees()
    rawcomp = ap.get_compass_raw()
    rawgyro = ap.get_gyroscope_raw()
    rawaccel = ap.get_accelerometer_raw()

    endtime = time()

    print(endtime - starttime)
    sleep(1)
