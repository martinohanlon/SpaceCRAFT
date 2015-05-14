from astro_pi import AstroPi

ap = AstroPi()

tempHumidity = ap.get_temperature_from_humidity()
tempPressure = ap.get_temperature_from_pressure()

print("Temp Humidity", tempHumidity)
print("Temp Pressure", tempPressure)

#hum = ap.get_humidity()

#print(hum)


