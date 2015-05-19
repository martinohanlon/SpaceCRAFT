from astro_pi import AstroPi

ap = AstroPi()

pressure = ap.get_pressure()

print("Pressure", pressure)



