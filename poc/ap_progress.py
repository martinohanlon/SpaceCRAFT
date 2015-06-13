#creating a 'progress bar' to show data was being collected
from astro_pi import AstroPi
from time import sleep

class AstroPiProgressBar():
    def __init__(self, ap, colour = [255,255,255]):
        self.ap = ap
        self.colour = colour
        self.reset()
        
    def next(self):
        self._clear_pixel()
        #increment x by step
        self.x += self.step_x
        #has x gone over the maximum or below the minimum
        if self.x < 0 or self.x > 7:
            #reverse x step
            self.step_x = self.step_x * -1
            #move x back
            self.x += self.step_x
            #increment y
            self.y += self.step_y
            #has y gone over the maximum or below the minimum
            if self.y < 0 or self.y > 7:
                #reverse y step
                self.step_y = self.step_y * -1
                #move y back
                self.y += self.step_y
        self._light_pixel()
            
    def reset(self):
        self.clear()
        self.x = 0
        self.y = 0
        self.step_x = 1
        self.step_y = 1
        self._light_pixel()

    def clear(self):
        self.ap.clear()

    def _light_pixel(self):
        #print("x = {} : y = {}".format(self.x,self.y))
        ap.set_pixel(self.x, self.y,    
                     self.colour[0], self.colour[1], self.colour[2])

    def _clear_pixel(self):
        ap.set_pixel(self.x, self.y, [0, 0, 0])

#test
if __name__ == "__main__":

    ap = AstroPi()

    progress = AstroPiProgressBar(ap)

    try:
        while(True):
            sleep(0.05)
            progress.next()
    finally:
        progress.clear()
