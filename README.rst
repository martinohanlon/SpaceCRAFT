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

e.g. to read in the file /home/pi/datafile.csv::

    sudo python3 astropidatareader.py /home/pi/datafile.csv

Interactive Minecraft Astro Pi
------------------------------

The spacecraft/mcinteractiveastropi.py creates a interactive astro pi in Minecraft which when hit (right clicked) with a sword it responds with a description and makes the interacts with the real astro pi.

Start Minecraft: Pi edition, select/create a new game::

    sudo python3 mcinteractiveastropi.py

The AstroPi model will appear above the player, fly up and hit the model to interact with it.

Documentation
=============

Astro Pi Data
-------------
The spacecraft.astropidata module contains 2 classes:

* AstroPiDataLogger - writing data from the astro pi computer to a file
* AstroPiDataReader - reading it back

Data structure
``````````````
The AstroPiDataLogger creates a `CSV`_ file which contains the following fields seperated by a comma . This structure can be read by the AstroPiDataReader.

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

AstroPiDataLogger
`````````````````
The data logger only contains one function, start(filename, timetorun, interval), which expects the following parameters to be passed:

* filename - the path and filename where the astro pi data is to be written
* timetorun - the time in seconds that the data logger should run for
* interval - how often in seconds the data logger should write to the file

To read data from the astro pi every 1 second for 180 seconds to the file /home/pi/astropidata.csv you would use the following code::
    #import AstroPiDataLogger
    from spacecraft.astropidata import AstroPiDataLogger
    
    #create the data logger
    logger = AstroPiDataLogger()
    
    #start the data logger
    logger.start("/home/pi/astropidata.csv", 180, 1)

AstroPiDataLogger can be made to print verbose progress messages by passing True when it is created::
    logger = AstroPiDataLogger(True)

AstroPiDataReader
`````````````````
TODO


Minecraft Models
----------------

SpaceCRAFT contains a number of minecraft models, in the spacecraft.mcmodels module, which you can include in your programs.

The following minecraft models are included:

* ISS - the international space station
* MCAstroPi - a Raspberry Pi with Astro Pi Sense HAT attached
* Rocket - a rocket similar to those drawn my children in the 80's
* LaunchPad - a launchpad for the rocket to sit on
* Arrow - a multicoloured arrow, really useful for showing the direction and orientation
* Stairs - a helter skelter styled stair case leading up

ISS, MCAstroPi, Rocket, LaunchPad, Arrow
````````````````````````````````````````
To create a model you need to pass a minecraft connection and a position of where you want the model::
    #import ISS model from spacecraft.mcmodels
    from spacecraft.mcmodels import ISS
    
    #import mcpi.minecraft module
    from mcpi.minecraft import Minecraft
    
    #create connection to minecraft
    mc = Minecraft.create()
    
    #get the players position, this will be where you create the model
    pos = mc.player.getTilePos()
    
    #create the ISS
    iss = ISS(mc, pos)

These models are all based on (inherited from) the minecraftstuff.MinecraftShape class and supports the following:

* move(x, y, z) - move the shape to a specific x, y, z
* moveBy(x, y, z) - move the shape by that number of blocks in x, y, z
* rotate(yaw, pitch, roll) - rotate the shape by a yaw, pitch and roll (in degrees)
* rotateBy(raw, pitch, roll) - rotate the shape by that angle
* clear() - clear the model
* draw() - draws the model if it has been cleared
* redraw() - redraws the model
* reset() - resets the model back to its original position and rotation
* setBlock(x, y, z, blockId, blockData) - sets a block within the model, the positions are relative not absolute
* setBlocks(x1, y1, z1, x2, y2, z2, blockId, blockData) - creates a suboid of blocks in the model, again positions are relative
* getShapeBlock(x, y, z) -> minecraftstuff.ShapeBlock - returns the block in the shape which is at that absolute position
* position -> mcpi.minecraft.Vec3(x, y, z) - the position of the shape in Minecraft
* visible -> boolean - whether the shape in visible

Rocket
``````
The rocket model can also be launched using the launch(height) function, height is the number of blocks the rocket should fly upwards::
    #import rocket model from spacecraft.mcmodels
    from spacecraft.mcmodels import Rocket
    
    #import mcpi.minecraft module
    from mcpi.minecraft import Minecraft
    
    #create connection to minecraft
    mc = Minecraft.create()
    
    #get the players position, this will be where you create the model
    pos = mc.player.getTilePos()
    
    #create the rocket
    rocket = Rocket(mc, pos)

    #launch the rocket 50 blocks up
    rocket.launch(50)

Stairs
``````
To create the stairs, you need to pass:

* a minecraft connection
* a position of the bottom of the stairs
* the width of the stairs - how many blocks each leg is
* the height - how many blocks the stairs should go up for
* a block type of what you want to stairs to be made from
* a optional block data value 

::
    #import Stairs from spacecraft.mcmodels
    from spacecraft.mcmodels import Stairs
    
    #import mcpi.minecraft and mcpi block modules
    from mcpi.minecraft import Minecraft
    from mcpi import block
    
    #create connection to minecraft
    mc = Minecraft.create()
    
    #get the players position, this will be where the stairs will start
    pos = mc.player.getTilePos()
    
    #create some stairs which have a width of 5 blocks, go up for 50 blocks and are made of STONE
    stairs = Stairs(mc, pos, 5, 50, block.STONE.id)


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
