from astro_pi import AstroPi

ap = AstroPi()

humidity = ap.get_humidity()

print("Humidity", humidity)



