#reading sensor data in a loop
from astro_pi import AstroPi
from time import sleep

ap = AstroPi()

while(True):
    pressure = ap.get_pressure()
    print(pressure)

    humidity = ap.get_humidity()
    print(humidity)

    temp = ap.get_temperature_from_pressure()
    print(temp)

    temp = ap.get_temperature_from_humidity()
    print(temp)

    orientation = ap.get_orientation_degrees()
    print(orientation["yaw"])
    print(orientation["pitch"])
    print(orientation["roll"])

    orientation = ap.get_orientation_radians()
    print(orientation["yaw"])
    print(orientation["pitch"])
    print(orientation["roll"])

    sleep(1)

