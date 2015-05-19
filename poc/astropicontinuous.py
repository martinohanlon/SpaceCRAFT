from astro_pi import AstroPi
from time import sleep

try:
    import thread
except ImportError:
    import _thread as thread

class AstroPiContinuous(AstroPi):
    """
    A class which continuously reads orientation data from AstroPi as without
    it the orientatin data looses sync
    """
    def __init__(self,
            fb_device='/dev/fb1',
            imu_settings_file='RTIMULib',
            text_assets='astro_pi_text',
            sample_rate = 0.1):

        AstroPi.__init__(self, fb_device, imu_settings_file, text_assets)
       
        self.sample_rate = sample_rate
        self.stopped = True
        self.running = False
        
    def start(self):
        """
        starts the thread that continuously reads the astro pi orientation data
        """
        #initialise the IMU by getting the orientation
        self.get_orientation()
        #start the orientation thread
        thread.start_new_thread(self._get_orientation_threaded, ())
        
    def _get_orientation_threaded(self):
        """
        reads the orientation data every sample rate to ensure astro pi is kept in sync
        """
        self.stopped = False
        self.running = True

        #keep reading the orientation data, this keeps AstroPi in sync
        while(not self.stopped):
            self.get_orientation()
            sleep(self.sample_rate)
            
        self.running = False
    
    def stop(self):
        """
        stops the continous read thread
        """
        self.stopped = True
        #wait for the thread to stop
        while(self.running):
            sleep(0.01)
            
    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.stop()

    def __del__(self):
        """
        A last ditch attempt to clean up the and stop the class glacefully at destruction
        this shouldnt be relied on and the object should be stopped properly
        """
        self.stop()
        
#test
if __name__ == "__main__":
    ap = AstroPiContinuous()
    ap.start()
    while(True):
        print(ap.get_orientation())
        sleep(1)
    
    with AstroPiContinuous() as ap:
        while(True):
            print(ap.get_orientation())
            sleep(2)
        
    
    
