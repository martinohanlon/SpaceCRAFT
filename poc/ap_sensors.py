from astro_pi import AstroPi

ap = AstroPi()

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

