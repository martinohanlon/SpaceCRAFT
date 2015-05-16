import argparse
from csv import DictWriter
from datetime import datetime
from time import sleep, time
from astro_pi import AstroPi
from astropiprogressbar import AstroPiProgressBar

class AstroPiDataLogger():

    #field name constants
    TIME = "time"
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

    #order of fieldnames for csv output file
    FIELDNAMES = [TIME,
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
                  ACCEL_RAW_Z]
    
    def __init__(self, verbose = False):

        self.verbose = verbose

        self._write_message("Astro Pi Data Logger")
        self._write_message("Starting Sense HAT")
        
        #create astro pi object
        self.ap = AstroPi()

        #set imu config (just in case anything has changed it!)
        self.ap.set_imu_config(True, True, True)

        #call get_humidity, get_pressure and get_orientation to init the sensors
        self.ap.get_humidity()
        self.ap.get_pressure()
        self.ap.get_orientation()

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

        #create the astro pi progress bar
        progressbar = AstroPiProgressBar(self.ap)
        
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

            #loop until the time to run as passed
            while((time() - starttime) < timetorun):

                #read data and write to csv file
                #todo there is better way of ensuring we get 1 per interval
                # the rowstarttime should be the starttime plus the interval
                rowstarttime = time()
                datarow = self._read_data()
                writer.writerow(datarow)
                
                #wait until the next interval
                while(time() - rowstarttime < interval):
                    #remove once astro pi bug is fixed
                    #keep getting the orientation
                    self.ap.get_orientation()
                    sleep(0.01)

                progressbar.next()

        progressbar.clear()
        
        self._write_message("Finished")

    def _read_data(self):
        """
        Internal. Reads data from the astro pi sensors and creates a dictionary of the fields
        """

        datarow = {}
        datarow[self.TIME] = datetime.now()
        
        datarow[self.HUMIDITY] = self.ap.get_humidity()
        datarow[self.PRESSURE] = self.ap.get_pressure()

        datarow[self.TEMP_HUMIDITY] = self.ap.get_temperature_from_humidity()
        datarow[self.TEMP_PRESSURE] = self.ap.get_temperature_from_pressure()

        orientation_rad = self.ap.get_orientation_radians()
        datarow[self.ORIENTATION_RAD_PITCH] = orientation_rad["pitch"]
        datarow[self.ORIENTATION_RAD_YAW] = orientation_rad["yaw"]
        datarow[self.ORIENTATION_RAD_ROLL] = orientation_rad["roll"]
        
        orientation_deg = self.ap.get_orientation_degrees()
        datarow[self.ORIENTATION_DEG_PITCH] = orientation_deg["pitch"]
        datarow[self.ORIENTATION_DEG_YAW] = orientation_deg["yaw"]
        datarow[self.ORIENTATION_DEG_ROLL] = orientation_deg["roll"]
        
        compass_raw = self.ap.get_compass_raw()
        datarow[self.COMPASS_RAW_X] = compass_raw["x"]
        datarow[self.COMPASS_RAW_Y] = compass_raw["y"]
        datarow[self.COMPASS_RAW_Z] = compass_raw["z"]

        gyro_raw = self.ap.get_compass_raw()
        datarow[self.GYRO_RAW_X] = gyro_raw["x"]
        datarow[self.GYRO_RAW_Y] = gyro_raw["y"]
        datarow[self.GYRO_RAW_Z] = gyro_raw["z"]

        accel_raw = self.ap.get_accelerometer_raw()
        datarow[self.ACCEL_RAW_X] = accel_raw["x"]
        datarow[self.ACCEL_RAW_Y] = accel_raw["y"]
        datarow[self.ACCEL_RAW_Z] = accel_raw["z"]

        return datarow

if __name__ == "__main__":

    #read command line options
    parser = argparse.ArgumentParser(description="Astro Pi Data Logger")
    parser.add_argument("filename", help="The output filename")
    parser.add_argument("timetorun", type=int, help="The time in seconds the logger should run for")
    parser.add_argument("interval", type=int, help="The time in seconds between each write")
    parser.add_argument("-v", "--verbose", action="store_true", help="Output verbose debug statements")
    args = parser.parse_args()

    #create the data logger object
    logger = AstroPiDataLogger(args.verbose)

    #start the data logger
    logger.start(args.filename, args.timetorun, args.interval)

