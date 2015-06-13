#testing the led matrix
from astro_pi import AstroPi

ap = AstroPi()

ap.clear()

#ap.show_message("Hello Space")

ap.set_pixel(0, 0, 255, 0, 0)

ap.set_pixel(7, 7, 255, 255, 255)

#ap.set_pixel(7, 7, 0, 0, 0)

ap.clear()

#ap.clear([0,0,255])
