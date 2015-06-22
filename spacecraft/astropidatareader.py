"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

astropidatareader.py

Program for reading in data logged by the AstroPiDataLogger
- its not invisaged that this progam will be used as all it does is output data to
  the screen, but it should be used as an example of how to use AstroPiDataReader
"""
import argparse
from astropidata import AstroPiDataReader

#data reader program
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Astro Pi Data Reader")
    parser.add_argument("filename", help="The input filename")
    parser.add_argument("-v", "--verbose", action="store_true", help="Output verbose debug statements")
    args = parser.parse_args()

    #open the file
    apreader = AstroPiDataReader(args.filename, args.verbose)

    #are there any rows?
    if apreader.rowcount > 0:
        #keep looping until its the end of file
        found_row = True
        while(found_row):
            #read the values
            datetime = apreader.get_datetime()
            time = apreader.get_time()
            cpu_temp = apreader.get_cpu_temperature()
            temp_humid = apreader.get_temperature_from_humidity()
            temp_press = apreader.get_temperature_from_pressure()
            pressure = apreader.get_pressure()
            humidity = apreader.get_humidity()
            ori_deg = apreader.get_orientation_in_degrees()
            ori_rad = apreader.get_orientation_in_radians()
            comp = apreader.get_compass_raw()
            gyro = apreader.get_gyroscope_raw()
            accel = apreader.get_accelerometer_raw()
            joystick = apreader.get_joystick()

            #print them to the screen
            print("{} {} {} {} {} {} {} {} {} {} {} {} {}".format(
                datetime,
                time,
                cpu_temp,
                temp_humid,
                temp_press,
                pressure,
                humidity,
                ori_deg,
                ori_rad,
                comp,
                gyro,
                accel,
                joystick))

            #move to the next row
            found_row = apreader.next()
    
