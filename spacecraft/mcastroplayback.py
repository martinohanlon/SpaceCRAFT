"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

mcastroplayback.py

Displays information captured from the Astro Pi board to a CSV file using the
astropidatalogger in Minecraft
"""

import sys
from mcpi.minecraft import Minecraft
from mcdisplays import ISSTowerMinecraftDisplay
from astropidata import AstroPiDataReader
from time import sleep, strftime, gmtime, time
from cmd import Cmd
from threading import Thread

class PlaybackData(Thread):
    def __init__(self, filename):
        #setup threading
        Thread.__init__(self)
        self.running = False
        self.stopped = True

        self.filename = filename
        self.speed = 1
        self.apr = None

    def run(self):
        #open the file
        self.running = True
        self.stopped = False

        try:
            #open astro pi data file
            apr = AstroPiDataReader(self.filename)
            self.apr = apr
            #are there any rows?
            if apr.rowcount > 0:
                
                #create connection to minecraft
                mc = Minecraft.create()

                mc.postToChat("Playback {} Started".format(self.filename))

                #find the position of where to put the ISS tower display
                pos = mc.player.getTilePos()
                pos.z -= 10
                pos.y = mc.getHeight(pos.x, pos.z)

                try:
                    #create the iss tower display
                    isstowerdisplay = ISSTowerMinecraftDisplay(mc, pos)

                    #loop until its stopped
                    found_row = True
                    while self.stopped == False and found_row == True:
                        #get the time started
                        real_time_start = time()
                        last_row_time = apr.get_time()
                        
                        #update the ISS dispay with the data
                        isstowerdisplay.update(
                            apr.get_time(),
                            apr.get_cpu_temperature(),
                            apr.get_temperature(),
                            apr.get_humidity(),
                            apr.get_pressure(),
                            apr.get_orientation(),
                            apr.get_joystick())
                        
                        #move onto the next row
                        found_row = apr.next()

                        #wait until the next row time
                        if found_row:
                            #wait until the time in the real world is greater than the time between the rows
                            while (time() - real_time_start) < ((apr.get_time() - last_row_time) / self.speed) :
                                sleep(0.001)
                finally:
                    isstowerdisplay.clear()
                    mc.postToChat("Playback {} finished".format(self.filename))
                    
            else:
                print("Error - {} contained no data".format(self.filename))

        #catch failed to open file error
        except IOError:
            print("Failed to open file '{}'.".format(self.filename))
            print(sys.exc_info()[1])

        #catch any other error
        except:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
                        
        finally:
            self.running = False
            self.stopped = True

    def stop(self):
        self.stopped = True
        #wait for it to stop running
        while self.running:
            sleep(0.01)

    def set_speed(self, speed):
        self.speed = speed
        
class PlaybackCommands(Cmd):
    """
    Manages the command line interface
    """

    SPEEDS = (1,2,4,8,16)
    
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "SpaceCRAFT $ "
        self.intro  = "Welcome to SpaceCRAFT data playback.  Type help or ? to list commands.\n"
        self.playback = None

    def do_exit(self, args):
        "Exit SpaceCRAFT playback:  exit"
        #if the playback is running stop it
        if self._is_playback_running():
            self.do_stop(1)
        return -1

    def do_play(self, args):
        "Play Astro Pi data file:  play filename"
        
        start_playback = False

        #is a file already running? If so, close it
        if self._is_playback_running():
            print("Error - Playback is already running")
        else:
            #open the file and start the playback
            filename, success = self._get_filename_arg(args)
            if success:
                self.playback = PlaybackData(filename)
                self.playback.start()
                sleep(1)
            else:
                print("Error - filename expected.  play filename")
                    
    def do_stop(self, args):
        "Stop Astro Pi data file playback:  stop"
        #if a file is running, stop it
        if self._is_playback_running():
            self.playback.stop()
            #wait for playback to stop
            self.playback.join()
        else:
            print("Error - no playback is running")
            
        self.playback = None

    def do_data(self, args):
        "Display the current data values:  data"
        if self._is_playback_running():
            print("Data values:")
            print(strftime("%d.%m.%y %H.%M.%S", 
                           gmtime(self.playback.apr.get_time())))
            print("cpu temp = {}".format(self.playback.apr.get_cpu_temperature()))
            print("temp = {}".format(self.playback.apr.get_temperature()))
            print("pressure = {}".format(self.playback.apr.get_pressure()))
            print("humidity = {}".format(self.playback.apr.get_humidity()))
            orientation = self.playback.apr.get_orientation()
            print("orientation = {},{},{}".format(
                orientation["pitch"],
                orientation["yaw"],
                orientation["roll"]))
        else:
            print("Error - no playback is running")
    
    def do_speed(self, args):
        "Set the playback speed (x1, x2, x4, x8, x16):  speed 2"
        #is a file already running?
        if self._is_playback_running():
            speed, success = self._get_speed_arg(args)
            if success:
                if self._is_valid_speed(speed):
                    self.playback.set_speed(speed)
                else:
                    print("Error - {} is not a valid speed".format(speed))
            else:
                print("Error - speed must be passed an number")
        else:
            print("Error - no playback is running")
        
    def emptyline(self):
        return False

    def _is_playback_running(self):
        if self.playback != None:
            if self.playback.running == True:
                return True
            else:
                return False
        else:
            return False
            
    def _get_filename_arg(self, args):
        try:
            if len(args) > 0:
                return args, True
            else:
                return args, False
        except:
            return args, False

    def _get_speed_arg(self, args):
        try:
            if len(args) > 0:
                speed = int(args)
                return speed, True
            else:
                return args, False
        except:
            return args, False

    def _is_valid_speed(self, speed):
        if speed in self.SPEEDS:
            return True
        else:
            return False
            
#main program
if __name__ == "__main__":
    PlaybackCommands().cmdloop()
