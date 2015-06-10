=========
SpaceCRAFT
=========

IN PROGRESS!!!

Todo. 

Conceived by Hannah Belshaw, from Cumnor House Girl’s School, created by Martin O'Hanlon, `Stuff about="code"`_.

Installation
============

Todo

Structure
=========

* spacecraft - the spacecraft python module and programs
* poc - proof of concept code used in the development
* scripts - useful scripts!

Usage
=====

Data logger
-----------

The spacecraft/astropidatalogger.py program reads data from the astro pi computer and writes it to a CSV files - it is run using::

    usage: astropidatalogger.py [-h] [-v] filename timetorun interval
   
    Astro Pi Data Logger
   
    positional arguments:
      filename       The output filename
      timetorun      The time in seconds the logger should run for
      interval       The time in seconds between each write

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  Output verbose debug statements


e.g. to run the data logger for 180 seconds reading data every 1 second::

    sudo python3 astropidatalogger.py /home/pi/datafile.csv 180 1

Data reader
-----------

The spacecraft/astropidatareader.py program reads CSV files created by the astropidatalogger.py program, its not invisage it is used to view data, but as a method for testing a file has been created successfully and as well as being an example of how to use the AstroPiDataReader::

    usage: astropidatareader.py [-h] [-v] filename
    
    Astro Pi Data Reader
    
    positional arguments:
      filename       The input filename
    
    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  Output verbose debug statements

e.g. to read in the file /home/pi/datafile.csv ::

    sudo python3 astropidatareader.py /home/pi/datafile.csv

Interactive Minecraft Astro Pi
------------------------------

The spacecraft/mcinteractiveastropi.py creates a interactive astro pi in Minecraft which when hit (right clicked) with a sword it responds with a description and makes the interacts with the real astro pi.

Start Minecraft: Pi edition, select/create a new game::

    sudo python3 mcinteractiveastropi.py


Documentation
=============

Data structure
--------------

The data logger program creates a `CSV`_ file which contains the following fields seperated by a comma (,).

===================== =========================== ===============================================
Python Constant       File Header                 Description
===================== =========================== ===============================================
TIME                  time                        time expressed as number of seconds since epoch
CPU_TEMP              cpu temperature             temperature of the raspberry pi cpu
HUMIDITY              humidity                    humidity
PRESSURE              pressure                    pressure
TEMP_HUMIDITY         temperature (humidity)      temperature in C from the humidity sensor
TEMP_PRESSURE         temperature (pressure)      temperature in C from the pressure sensor
ORIENTATION_RAD_PITCH orientation radians pitch   pitch in radians
ORIENTATION_RAD_YAW   orientation radians yaw     yaw in radians
ORIENTATION_RAD_ROLL  orientation radians roll    roll in radians
ORIENTATION_DEG_PITCH orientation degrees pitch   pitch in degrees
ORIENTATION_DEG_YAW   orientation degrees yaw     yaw in degrees
ORIENTATION_DEG_ROLL  orientation degrees roll    roll in degrees
COMPASS_RAW_X         compass raw x               raw x from compass
COMPASS_RAW_Y         compass raw y               raw y from compass
COMPASS_RAW_Z         compass raw z               raw z from compass
GYRO_RAW_X            gyroscope raw x             raw x from gyroscope
GYRO_RAW_Y            gyroscope raw y             raw y from gyroscope
GYRO_RAW_Z            gyroscope raw z             raw z from gyroscope
ACCEL_RAW_X           accelerometer raw x         raw x from accelerometer
ACCEL_RAW_Y           accelerometer raw y         raw y from accelerometer
ACCEL_RAW_Z           accelerometer raw z         raw z from accelerometer
JOYSTICKUP            joystick up                 1 if the joystick was pushed up else 0
JOYSTICKDOWN          joystick down               1 if the joystick was pushed down up else 0
JOYSTICKRIGHT         joystick right              1 if the joystick was pushed right else 0
JOYSTICKLEFT          joystick left               1 if the joystick was pushed left else 0
JOYSTICKBUTTON        joystick button             1 if the joystick button was pushed else 0
===================== =========================== ===============================================

The Python Constant is used in conjunction with the AstroPiLogger and AstroPiReader classes to reference fields.
The File Header is output on the first row the CSV file.

Contributors
============

* `Martin O'Hanlon`_
* Hannah Belshaw

Open Source
===========

* The code is licensed under the `BSD Licence`_
* The project source code is hosted on `GitHub`_
* Please use `GitHub issues`_ to submit bugs and report issues

.. _Raspberry Pi: https://www.raspberrypi.org/
.. _Astro Pi: http://www.astro-pi.org/
.. _Martin O'Hanlon: https://github.com/martinohanlon
.. _BSD Licence: http://opensource.org/licenses/BSD-3-Clause
.. _GitHub: https://github.com/martinohanlon/SpaceCRAFT
.. _GitHub Issues: https://github.com/martinohanlon/SpaceCRAFT/issues
.. _Stuff about="code": http://www.stuffaboutcode.com
.. _CSV: http://en.wikipedia.org/wiki/Comma-separated_values