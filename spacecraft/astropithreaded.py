"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

astropithreaded.py

A class which continually reads the Astro Pi's orientation otherwise it goes out of sync
"""
try: 
    from sense_hat import AstroPi
except ImportError:
    print("Error importing sense_hat module - required for AstroPiThreaded")

from time import sleep

try:
    import thread
except ImportError:
    import _thread as thread

class AstroPiThreaded(AstroPi):
    """
    A class which continually reads the Astro Pi's orientation otherwise it goes out of sync
    """
    def __init__(
        self,
        imu_settings_file = 'RTIMULib',
        text_assets = 'sense_hat_text',
        sample_rate = 0.01):

        self.sample_rate = sample_rate
        
        AstroPi.__init__(self, imu_settings_file, text_assets)

        self._orientation = AstroPi.get_orientation(self)

        #start the orientation thread
        thread.start_new_thread(self._get_orientation_threaded, ())

    def _get_orientation_threaded(self):
        """
        Internal. called in a thread to continuously read the astro pi data
        """
        self.stopped = False
        self.running = True
        while(not self.stopped):
            self._orientation = AstroPi.get_orientation(self)
            sleep(self.sample_rate)
        self.running = False
    
    def get_orientation(self):
        """
        Returns the orientation data from the last time it was read by the thread
        """
        return self._orientation

    def stop(self):
        """
        Stops the thread
        """
        self.stopped = True
        #wait for the thread to stop
        while self.running:
            sleep(0.01)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.stop() 
        
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
    
