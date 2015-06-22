"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

astropidata.py

Classes for writing astro pi data to CSV files and reading it back again

astro_pi module is required for AstroPiDataLogger but not for AstroPiDataReader
"""
from csv import DictWriter, DictReader
from datetime import datetime
from time import sleep, time

try: 
    from astropithreaded import AstroPiThreaded
except ImportError:
    print("Error importing astro_pi module - required for AstroPiDataLogger")

from astropiprogressbar import AstroPiBelshawProgressBar
from cputemp import CPUTemp
import pygame
from pygame.locals import *

#field name constants
DATETIME = "datetime"
TIME = "time"
CPU_TEMP = "cpu temperature"
HUMIDITY = "humidity"
PRESSURE = "pressure"
TEMP_HUMIDITY = "temperature (humidity)"
TEMP_PRESSURE = "temperature (pressure)"
ORIENTATION_RAD_PITCH = "orientation radians pitch"
ORIENTATION_RAD_YAW = "orientation radians yaw"
ORIENTATION_RAD_ROLL = "orientation radians roll"
ORIENTATION_DEG_PITCH = "orientation degrees pitch"
ORIENTATION_DEG_YAW = "orientation degrees yaw"
ORIENTATION_DEG_ROLL = "orientation degrees roll"
COMPASS_RAW_X = "compass raw x"
COMPASS_RAW_Y = "compass raw y"
COMPASS_RAW_Z = "compass raw z"
GYRO_RAW_X = "gyroscope raw x"
GYRO_RAW_Y = "gyroscope raw y"
GYRO_RAW_Z = "gyroscope raw z"
ACCEL_RAW_X = "accelerometer raw x"
ACCEL_RAW_Y = "accelerometer raw y"
ACCEL_RAW_Z = "accelerometer raw z"
JOYSTICKUP = "joystick up"
JOYSTICKDOWN = "joystick down"
JOYSTICKRIGHT = "joystick right"
JOYSTICKLEFT = "joystick left"
JOYSTICKBUTTON = "joystick button"

class AstroPiDataLogger():
    """
    A data logger for the astro pi board
    """
    #order of fieldnames for csv output file
    FIELDNAMES = [DATETIME,
                  TIME,
                  CPU_TEMP,
                  HUMIDITY,
                  PRESSURE,
                  TEMP_HUMIDITY,
                  TEMP_PRESSURE,
                  ORIENTATION_RAD_PITCH,
                  ORIENTATION_RAD_YAW,
                  ORIENTATION_RAD_ROLL,
                  ORIENTATION_DEG_PITCH,
                  ORIENTATION_DEG_YAW,
                  ORIENTATION_DEG_ROLL,
                  COMPASS_RAW_X,
                  COMPASS_RAW_Y,
                  COMPASS_RAW_Z,
                  GYRO_RAW_X,
                  GYRO_RAW_Y,
                  GYRO_RAW_Z,
                  ACCEL_RAW_X,
                  ACCEL_RAW_Y,
                  ACCEL_RAW_Z,
                  JOYSTICKUP,
                  JOYSTICKDOWN,
                  JOYSTICKRIGHT,
                  JOYSTICKLEFT,
                  JOYSTICKBUTTON]
    
    def __init__(self, verbose = False):

        self.verbose = verbose

        self._write_message("Astro Pi Data Logger")

        self._init_pygame()

    def _write_message(self, message):
        """
        Internal. Prints a message to stdout if the verbose flag has been set.
        """

        if self.verbose:
            print(message)
    
    def start(self, filename, timetorun, interval):
        """
        Starts the data logger, runs for the 'time to run' in seconds, writing data every 'interval' seconds. 
        """

        #create astro pi object
        self._write_message("Starting Sense HAT")
        #use the threaded astro pi class, so orientation stay in sync
        ap = AstroPiThreaded()

        #create the astro pi progress bar
        progressbar = AstroPiBelshawProgressBar(ap)

        try:

            self._write_message("Initialising Sense HAT")
            self._init_astro_pi(ap)

            #open cpu temperature file
            self._write_message("Opening CPU temperature")
            with CPUTemp() as cpu_temp:
            
                self._write_message("Starting data logger")
                self._write_message(" filename - {}".format(filename))
                self._write_message(" time to run - {} seconds".format(timetorun))
                self._write_message(" interval - {} seconds".format(interval))

                #open file for writing
                self._write_message("Creating file {}".format(filename))
                with open(filename, "w") as datafile:
                    
                    #create the writer
                    writer = DictWriter(datafile, fieldnames = self.FIELDNAMES)
                    
                    #write the csv file header
                    writer.writeheader()

                    #get the time the program started
                    starttime = time()  

                    self._write_message("Writing data")

                    nextrowtime = starttime
                    #loop until the time to run as passed
                    while((time() - starttime) < timetorun):

                        #read data and write to csv file
                        datarow = self._read_data(ap, cpu_temp)
                        writer.writerow(datarow)
                        
                        #wait until the next interval
                        nextrowtime = nextrowtime + interval
                        while(time() < nextrowtime):
                            sleep(0.01)

                        progressbar.next()
                
        finally:
            #stop the astro pi thread which reads the orientation
            ap.stop()

            #clear the progress bar 
            progressbar.clear()
                    
            self._write_message("Finished")

    def _init_astro_pi(self, ap):
        #set imu config (just in case anything has changed it!)
        ap.set_imu_config(True, True, True)

        #call get_humidity, get_pressure and get_orientation to init the sensors
        ap.get_humidity()
        ap.get_pressure()
        ap.get_orientation()

    def _init_pygame(self):
        pygame.init()
        
        pygame.display.set_mode((640, 480))

        pygame.event.set_allowed(KEYUP)

    def _read_data(self, ap, cpu_temp):
        """
        Internal. Reads data from the astro pi sensors and creates a dictionary of the fields
        """

        datarow = {}

        datarow[DATETIME] = datetime.now()
        
        datarow[TIME] = time()

        datarow[CPU_TEMP] = cpu_temp.get_temperature()
        
        datarow[HUMIDITY] = ap.get_humidity()
        datarow[PRESSURE] = ap.get_pressure()

        datarow[TEMP_HUMIDITY] = ap.get_temperature_from_humidity()
        datarow[TEMP_PRESSURE] = ap.get_temperature_from_pressure()

        orientation_rad = ap.get_orientation_radians()
        datarow[ORIENTATION_RAD_PITCH] = orientation_rad["pitch"]
        datarow[ORIENTATION_RAD_YAW] = orientation_rad["yaw"]
        datarow[ORIENTATION_RAD_ROLL] = orientation_rad["roll"]
        
        orientation_deg = ap.get_orientation_degrees()
        datarow[ORIENTATION_DEG_PITCH] = orientation_deg["pitch"]
        datarow[ORIENTATION_DEG_YAW] = orientation_deg["yaw"]
        datarow[ORIENTATION_DEG_ROLL] = orientation_deg["roll"]
        
        compass_raw = ap.get_compass_raw()
        datarow[COMPASS_RAW_X] = compass_raw["x"]
        datarow[COMPASS_RAW_Y] = compass_raw["y"]
        datarow[COMPASS_RAW_Z] = compass_raw["z"]

        gyro_raw = ap.get_gyroscope_raw()
        datarow[GYRO_RAW_X] = gyro_raw["x"]
        datarow[GYRO_RAW_Y] = gyro_raw["y"]
        datarow[GYRO_RAW_Z] = gyro_raw["z"]

        accel_raw = ap.get_accelerometer_raw()
        datarow[ACCEL_RAW_X] = accel_raw["x"]
        datarow[ACCEL_RAW_Y] = accel_raw["y"]
        datarow[ACCEL_RAW_Z] = accel_raw["z"]

        datarow[JOYSTICKUP] = 0
        datarow[JOYSTICKDOWN] = 0
        datarow[JOYSTICKRIGHT] = 0
        datarow[JOYSTICKLEFT] = 0
        datarow[JOYSTICKBUTTON] = 0
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_DOWN:
                    datarow[JOYSTICKDOWN] = 1
                elif event.key == pygame.K_UP:
                    datarow[JOYSTICKUP] = 1
                elif event.key == pygame.K_LEFT:
                    datarow[JOYSTICKLEFT] = 1
                elif event.key == pygame.K_RIGHT:
                    datarow[JOYSTICKRIGHT] = 1
                elif event.key == pygame.K_RETURN:
                    datarow[JOYSTICKBUTTON] = 1

        return datarow

class AstroPiDataReader():
    """
    Reads data from the CSV file created by the AstroPiDataLogger
    """
    def __init__(self, filename, verbose = False):
        self.filename = filename
        self.verbose = verbose

        #open the file and read it into a list, so we can iterate it
        self._write_message("Reading file {}".format(filename))
        
        self.datalist = []
        with open(filename, "r") as datafile:
            reader = DictReader(datafile)
            for row in reader:
                self.datalist.append(row)

        self._write_message("Complete - {} rows".format(len(self.datalist)))

        self.currentrow = 0
        
    def _write_message(self, message):
        """
        Internal. Prints a message to stdout if the verbose flag has been set.
        """
        if self.verbose:
            print(message)

    def next(self):
        """
        Moves onto the next row. Return True if successful
        """
        #are there any more rows left
        if (len(self.datalist) - 1) > self.currentrow:
            self.currentrow += 1
            return True
        else:
            return False

    def previous(self):
        """
        Moves back to the previous row. Return True if successful
        """
        if currentrow > 0:
            self.currentrow -= 1
            return True
        else:
            return False

    @property
    def rowcount(self):
        return len(self.datalist)

    @property
    def data(self):
        return self.datalist[self.currentrow]

    def get_datetime(self):
        return self.data[DATETIME]

    def get_time(self):
        return float(self.data[TIME])
    
    def get_temperature(self):
        return self.get_temperature_from_humidity()

    def get_temperature_from_humidity(self):
        return float(self.data[TEMP_HUMIDITY])

    def get_temperature_from_pressure(self):
        return float(self.data[TEMP_PRESSURE])
    
    def get_pressure(self):
        return float(self.data[PRESSURE])

    def get_humidity(self):
        return float(self.data[HUMIDITY])
    
    def get_orientation_in_degrees(self):
        return {"pitch": float(self.data[ORIENTATION_DEG_PITCH]),
                "yaw": float(self.data[ORIENTATION_DEG_YAW]),
                "roll": float(self.data[ORIENTATION_DEG_ROLL])}

    def get_orientation_in_radians(self):
        return {"pitch": float(self.data[ORIENTATION_RAD_PITCH]),
                "yaw": float(self.data[ORIENTATION_RAD_YAW]),
                "roll": float(self.data[ORIENTATION_RAD_ROLL])}

    def get_orientation(self):
        return self.get_orientation_in_degrees()

    def get_compass_raw(self):
        return {"x": float(self.data[COMPASS_RAW_X]),
                "y": float(self.data[COMPASS_RAW_Y]),
                "z": float(self.data[COMPASS_RAW_Z])}

    def get_gyroscope_raw(self):
        return {"x": float(self.data[GYRO_RAW_X]),
                "y": float(self.data[GYRO_RAW_Y]),
                "z": float(self.data[GYRO_RAW_Z])}

    def get_accelerometer_raw(self):
        return {"x": float(self.data[ACCEL_RAW_X]),
                "y": float(self.data[ACCEL_RAW_Y]),
                "z": float(self.data[ACCEL_RAW_Z])}

    def get_cpu_temperature(self):
        return float(self.data[CPU_TEMP])

    def get_joystick(self):
        return {"up": int(self.data[JOYSTICKUP]),
                "down": int(self.data[JOYSTICKDOWN]),
                "left": int(self.data[JOYSTICKLEFT]),
                "right": int(self.data[JOYSTICKRIGHT]),
                "button": int(self.data[JOYSTICKBUTTON])}
