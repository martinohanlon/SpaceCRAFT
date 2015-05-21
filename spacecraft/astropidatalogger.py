"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

astropidatalogger.py

A data logging program which will write data from the astro pi board to
a CSV file.

A class for reading the data files which have been written
"""
import argparse
from astropidata import AstroPiDataLogger

#data logger program
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

