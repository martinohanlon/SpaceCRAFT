"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

astropithreaded.py

A class which continually reads the Astro Pi's orientation otherwise it goes out of sync
"""
from astro_pi import AstroPi
from time import sleep

try:
    import thread
except ImportError:
    import _thread as thread

class AstroPiThreaded(AstroPi):
    """
    A class which continually reads the Astro Pi's orientation otherwise it goes out of sync
    """
    
    def __init__(self,
            fb_device='/dev/fb1',
            imu_settings_file='RTIMULib',
            text_assets='astro_pi_text'):
                
        AstroPi.__init__(self, fb_device, imu_settings_file, text_assets)

        self._orientation = AstroPi.get_orientation(self)

        #start the orientation thread
        thread.start_new_thread(self._get_orientation_threaded, ())

    def _get_orientation_threaded(self):
        self.stopped = False
        while(not self.stopped):
            self._orientation = AstroPi.get_orientation(self)
            sleep(0.01)
    
    def get_orientation(self):
        return self._orientation

    def stop(self):
        self.stopped = True
        
#test
if __name__ == "__main__":
    ap = AstroPiThreaded()
    try:
        while True:
            print(ap.get_orientation())
            #print(ap.get_temperature())
            sleep(0.1)
    finally:
        ap.stop()
    
