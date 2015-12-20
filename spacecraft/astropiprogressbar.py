"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

astropiprogressbar.py

Progress bars which shows an animation on the astro pi led matrix
used to show the data logger is working
"""
from sense_hat import AstroPi
from time import sleep

class AstroPiProgressBar():
    """
    A simple progress bar, which progresses each time the .next function is called
    """
    def __init__(self, ap, colour = [255,255,255]):
        self.ap = ap
        self.colour = colour
        self.reset()
        
    def next(self):
        """
        Increments the progress bar by 1
        """
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
        """
        Resets the progress bar
        """
        self.clear()
        self.x = 0
        self.y = 0
        self.step_x = 1
        self.step_y = 1
        self._light_pixel()

    def clear(self):
        """
        Clears the led matrix
        """
        self.ap.clear()

    def _light_pixel(self):
        """
        Internal. Lights a pixel to show progress
        """
        #print("x = {} : y = {}".format(self.x,self.y))
        self.ap.set_pixel(self.x, self.y,    
                     self.colour[0], self.colour[1], self.colour[2])

    def _clear_pixel(self):
        """
        Internal. Clears a pixel
        """
        self.ap.set_pixel(self.x, self.y, [0, 0, 0])

class AstroPiBelshawProgressBar():
    """
    A progress bar using an animation created and coded by Hannah and John Belshaw which is used as a progress bar
    """
    def __init__(self, ap):
        self.ap = ap
        self.reset()
        self.launchCount = 0
        self.step = 1

        #constants for colours B = Black, g = green, b = blue, r = red
        B = [0, 0, 0]
        g = [0, 100, 0]
        b = [0, 0, 255]
        r = [255, 0, 0]

        #build the animation sequence
        launch = []
        launch.append([
            g, r, r, B, B, r, r, g,
            r, g, B, B, B, B, g, r,
            r, B, g, B, B, g, B, r,
            B, B, B, g, g, B, B, B,
            B, B, B, g, g, B, B, B,
            r, B, g, B, B, g, B, r,
            r, g, B, B, B, B, g, r,
            g, r, r, B, B, r, r, g])

        launch.append([
            g, B, B, B, B, B, B, g,
            B, g, r, B, B, r, g, B,
            B, r, g, B, B, g, r, B,
            B, B, B, g, g, B, B, B,
            B, B, B, g, g, B, B, B,
            B, r, g, B, B, g, r, B,
            B, g, r, B, B, r, g, B,
            g, B, B, B, B, B, B, g])

        launch.append([
            g, B, B, B, B, B, B, g,
            B, g, B, B, B, B, g, B,
            B, B, g, r, r, g, B, B,
            B, B, r, g, g, r, B, B,
            B, B, r, g, g, r, B, B,
            B, B, g, r, r, g, B, B,
            B, g, B, B, B, B, g, B,
            g, B, B, B, B, B, B, g])

        launch.append([
            g, B, B, B, B, B, B, g,
            B, g, B, B, B, B, g, B,
            B, B, g, B, B, g, B, B,
            B, B, B, r, r, B, B, B,
            B, B, B, r, r, B, B, B,
            B, B, g, B, B, g, B, B,
            B, g, B, B, B, B, g, B,
            g, B, B, B, B, B, B, g])

        launch.append([
            g, B, B, B, B, B, B, g,
            B, g, B, B, B, B, g, B,
            B, B, g, B, B, g, B, B,
            B, B, B, g, g, B, B, B,
            B, B, B, g, g, B, B, B,
            B, B, g, B, B, g, B, B,
            B, g, B, B, B, B, g, B,
            g, B, B, B, B, B, B, g])

        self.launch = launch
        
    def next(self):
        """
        Increments the progress bar by 1
        """

        #draw the current launch
        self._draw()
        
        #increment the count
        self.launchCount += self.step

        #have we got to the end? If so, change the step to go backwards
        if self.launchCount == 4:
            self.step = -1

        #have we got back to the start?
        if self.launchCount == 0:
            self.step = 1
            
    def _draw(self):
        """
        Internal. Draws the animation launch frame onto the led matrix 
        """
        self.ap.set_pixels(self.launch[self.launchCount])

    def reset(self):
        """
        Resets the progress bar
        """
        self.clear()
        self.launchCount = 0
        self.step = 1
        
    def clear(self):
        """
        Clears the led matrix
        """
        self.ap.clear()

#test
if __name__ == "__main__":

    ap = AstroPi()

    progress = AstroPiProgressBar(ap)

    try:
        for count in range(0,10):
            sleep(0.1)
            progress.next()
    finally:
        progress.clear()

    belshawProgress = AstroPiBelshawProgressBar(ap)

    try:
        for count in range(0,10):
            sleep(0.1)
            belshawProgress.next()
    finally:
        belshawProgress.clear()

