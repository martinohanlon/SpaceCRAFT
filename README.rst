==========
SpaceCRAFT
==========

SpaceCRAFT is a python module and collection of programs which displays data from the `Raspberry Pi`_ `Astro Pi`_ computer in `Minecraft Pi Edition`_.

SpaceCRAFT was conceived by Hannah Belshaw, from Cumnor House Girls School, and was the `Primary School Winning Entry`_ in the `Astro Pi`_ competition, it was created by Martin O'Hanlon (`Stuff about=code`_) for the `Raspberry Pi`_ foundation.

Structure
=========

* spacecraft - the spacecraft python module and programs
* poc - proof of concept code used in the development included for interest and prosperity
* scripts - useful scripts!

Installation
============

To download SpaceCRAFT, clone the source code from `GitHub`_::

    cd ~
    git clone https://github.com/martinohanlon/SpaceCRAFT

To install the spacecraft python module which will allow you to remix or create your own SpaceCRAFT displays::

    cd ~/SpaceCRAFT
    sudo python2 setup.py install
    sudo python3 setup.py install

All the program files are contained in the ~/SpaceCRAFT/spacecraft directory::

    cd ~/SpaceCRAFT/spacecraft

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

Minecraft Data Playback
-----------------------
The spacecraft/mcastroplayback.py program playbacks data from a CSV file created by the Data Logger and displays the information into Minecraft using the towers, clock, ISS and rocket design conceived by Hannah. This is the program which you can use to playback the data which is returned from on the AstroPi computer from the ISS.

The program has a command line interface which is run from the terminal using::

    sudo python3 mcastroplayback.py

When it starts it will show the following prompt::

    Welcome to SpaceCRAFT data playback.  Type help or ? to list commands.
    
    SpaceCRAFT $

Typing the command help and pressing Enter will display all the playback commands::

    SpaceCRAFT $ help
    
    Documented commands (type help <topic>):
    ========================================
    data  exit  help  play  speed  stop

Typing help and the name of a command will display information about how to use that command, e.g.::

    SpaceCRAFT $ help play
    Play Astro Pi data file:  play filename

To playback a file use the play command and the location of the file, e.g.::

    SpaceCRAFT $ play /home/pi/datafile.csv

To stop the playback use the stop command::

    SpaceCRAFT $ stop

To exit the program use the exit command::

    SpaceCRAFT $ exit

Minecraft Real-Time Data Display
--------------------------------
The spacecraft/realtimedisplay.py programs reads data from the Astro Pi Sense HAT in real time and displays the information into Minecraft using the towers, clock, ISS and rocket design conceived by Hannah::

    sudo python3 mcastrorealtime.py

Interactive Minecraft Astro Pi
------------------------------
The spacecraft/mcinteractiveastropi.py program creates a interactive astro pi in Minecraft which when hit (right clicked) with a sword it responds with a description and makes the interacts with the real astro pi.

Start Minecraft: Pi edition, select/create a new game and run::

    sudo python3 mcinteractiveastropi.py

The AstroPi model will appear above the player, fly up and hit the model to interact with it.

Minecraft Rocket Launch
-----------------------
The spacecraft/mcrocketlaunch.py program simulates a rocket launch including pitching over the rocket as it ascends. Run using::

    sudo python3 mcrocketlaunch.py

When the program runs a rocket will be created in Minecraft sitting on a launch pad.  To launch the rocket the player has to hit (right click while holding a sword) the launch pad.

SpaceCRAFT Python Module
========================
The SpaceCRAFT project contains a Python module called spacecraft which you can use to create your own Astro Pi Minecraft projects.

The module contains the following sub modules:

* astropidata - used to log data from the astro pi computer to a CSV file and read it back again
* astropithreaded - a threaded version of the AstroPi module which is useful for reading data continuously from the Astro Pi computer
* cputemp - used to read the temperature of the CPU
* mcclock - a minecraft clock which can be used to show the date and time
* mcmodels - minecraft models which can we be reused
* mcsensors - builds in the minecraft which can be used to display values from the astro pi sensors

Astro Pi Data (astropidata)
---------------------------
The spacecraft.astropidata module contains 2 classes:

* AstroPiDataLogger - writing data from the astro pi computer to a file
* AstroPiDataReader - reading it back

AstroPiDataLogger
`````````````````
The AstroPiDataLogger::

    AstroPiDataLogger(verbose = False)

It is started by using the start() function and expects the following parameters to be passed:

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
The AstroPiDataReader reads data files created by the AstroPiDataLogger::

    AstroPiDataReader(filename, verbose = False)

An open file error will be returned in the file cannot be opened. 

When the file is open it can be iterated and read using the following functions:

* rowcount -> integer - returns the number of rows in the file
* next() -> bool - moves to the next row in the file, returns False if there are no more rows
* previous() -> bool - moves to the previous row in the, returns False if at the start of the file
* currentrow -> integer - returns a 0 based value for the current row
* get_datetime -> string - returns a string representing the time in the format %d/%M/%Y %h:%m:%s
* get_time() -> integer - returns the time the row was created, in seconds since the epoch
* get_temperature() -> float - returns the temperature in C
* get_temperature_from_humidity() -> float - returns the temperature in C from the humidity sensor
* get_temperature_from_pressure() -> float - returns the temperature in C from the pressure sensor
* get_pressure() -> float - returns the pressure
* get_humidity() -> float - returns the humidity
* get_orientation() -> dict - returns the orientation in degress as a dictionary of "pitch", "yaw", "roll"
* get_orientation_in_degrees() -> dict - returns the orientation in degress as a dictionary of "pitch", "yaw", "roll"
* get_orientation_in_radians() -> dict - returns the orientation in radians as a dictionary of "pitch", "yaw", "roll"
* get_compass_raw() -> dict - returns the raw compass values as a dictionary of "x", "y", "z"
* get_gyroscope_raw() -> dict - returns the raw gyroscope values as a dictionary of "x", "y", "z"
* get_accelerometer_raw() -> dict - returns the raw accelerometer values as a dictionary of "x", "y", "z"
* get_cpu_temperature() -> float - returns the temperature of the cpu
* get_joystick() -> dict - returns whether the joystick was pressed (1 for pressed, 0 for not pressed) as dictionary of "up", "down", "left", "right", "button"

To loop through each row in a data file and print it to the screen you would use the following code::

    #import AstroPiDataReader
    from spacecraft.astropidata import AstroPiDataReader
    
    #create the data reader
    reader = AstroPiDataReader("/home/pi/astropidata.csv")

    #are there any rows?
    if reader.rowcount > 0:

        #keep looping until its the end of file
        found_row = True
	        while(found_row):

            #get the time the row was created
            timedata = reader.get_datetime()
            print("Time = {}".format(timedata))
    
            #move to the next row
            found_row = reader.next()

Data file
`````````
AstroPiDataLogger creates a `CSV`_ file which contains the following fields seperated by a comma . This structure can be read by the AstroPiDataReader as well as text editors (such as Leafpad or Notepad) and spreadsheet applications (Excel, Sheet).

===================== =========================== ===============================================
Python Constant       File Header                 Description
===================== =========================== ===============================================
DATETIME              datetime                    datetime string in format %d/%M/%Y %h:%m:%s
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

The Python Constant is used internally within the AstroPiLogger and AstroPiReader classes to reference fields.
The File Header is output on the first row the CSV file.

Astro Pi Threaded (astropithreaded)
-----------------------------------
The astropithreaded module allows you to continuously read orientation data from the Astro Pi Sense HAT and it not go out of sync as in order to get accurate data from the IMU it should be called greater than the gyro sample rate. 

The AstroPiThreaded class does this by creating a thread which reads data quicker than the sample rate and as it inherits form the AstroPi class it also supports all the same methods.

As AstroPiThreaded spawns a seperate thread its important the stop() function is used when your program finishes.

::

    from spacecraft.astropithreaded import AstroPiThreaded
    from time import sleep
    ap = AstroPiThreaded()
    try: 
        while True:
            print(ap.get_orientation())
            sleep(1)
    finally:
        ap.stop()

CPU Temperature (cputemp)
-------------------------
To supplement the astropi data SpaceCRAFT also reads the CPU temperature using the the CPUTemp class in the cputemp module. Its a very quick way of reading the cpu temperature.

::

    #import the cputemp module
    from cputemp import CPUTemp

    #create the CPUTemp object and read the temperature in C & F
    with CPUTemp() as cpu_temp:
        print("{} C".format(cpu_temp.get_temperature()))
        print("{} F".format(cpu_temp.get_temperature_in_f()))

Minecraft Clock (mcclock)
-------------------------
SpaceCRAFT includes a 'digital' clock to display the date and time, it is created by passing a minecraft connection (mc), position and block type to the Clock class. The methods setTime(time) and updateTime() can be used to set the time to any date and time, or update the time to the current date and time::

    #import modules
    from mcpi.minecraft import Minecraft
    from mcpi import block
    from mcclock import Clock
    from time import time

    #create connection to minecraft
    mc = Minecraft.create()
    #get the players position and add 12 to Y as the clock is 11 blocks high
    pos = mc.player.getTilePos()
    pos.y += 12

    #create the clock
    clock = Clock(mc, pos, block.WOOL.id, 2)
    
    #set the time to now (or any 'time')
    clock.setTime(time())

    #update the time
    clock.updateTime()

Minecraft Models (mcmodels)
---------------------------
SpaceCRAFT contains a number of minecraft models, in the spacecraft.mcmodels module, which you can include in your programs:

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

These models are all based on (inherited from) the minecraftstuff.MinecraftShape class and support the following:

* move(x, y, z) - move the shape to a specific x, y, z
* moveBy(x, y, z) - move the shape by that number of blocks in x, y, z
* rotate(yaw, pitch, roll) - rotate the shape by a yaw, pitch and roll (in degrees)
* rotateBy(raw, pitch, roll) - rotate the shape by that angle
* clear() - clear the model
* draw() - draws the model if it has been cleared
* redraw() - redraws the model
* reset() - resets the model back to its original position and rotation
* setBlock(x, y, z, blockId, blockData) - sets a block within the model, the positions are relative not absolute
* setBlocks(x1, y1, z1, x2, y2, z2, blockId, blockData) - creates a cuboid of blocks in the model, again positions are relative
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

Minecraft Sensor Displays (mcsensors)
-------------------------------------
There are a the following minecraft models in the spacecraft.mcsensors module for displaying sensor data in Minecraft:

* DisplayTube - a glass tube which fills with a block type (a bit like a thermometer!)
* BarGraph - a bar graph built using blocks
* SpikeyCircle - data is displayed as lines which rotate out from the centre of a circle

DisplayTube
```````````
To create a DisplayTube you need pass:

* mc - minecraft connection
* pos - position to create the DisplayTube
* height - the height of the display tube
* minValue - the minimum value the display tube should show
* maxValue - the maximum value 
* blockId - the id of the block the tube should fill with
* blockData (optional) - the data value of the block

Based on the height, minValue and maxValue the BarGraph will scale the number of blocks

The DisplayTube has 2 methods:

* addValue(value) - add 1 value to the BarGraph, if the value is above or below the maxValue or minValue it will change the min / max values to the current value
* clear() - clears the DisplayTube

::

    from spacecraft.mcsensors import BarGraph
    from mcpi.minecraft import Minecraft
    from time import sleep

    #create connection to minecraft
    mc = Minecraft.create()
    #find the players position
    pos = mc.player.getTilePos()

    #create the display tube
    height = 10
    minValue = 0
    maxValue = 10
    tube = DisplayTube(mc, pos, 10, 0, 10, block.LAVA.id)

    #set some values in the tube
    sleep(5)
    for count in range(0,11):
        tube.setValue(count)
        sleep(1)

   tube.clear()

BarGraph
````````
To create a BarGraph the minimum values which have to be passed are:

* mc - minecraft connection
* pos - position to create the BarGraph
* height - the height of the bar graph
* maxLength - the maximum length of the bar graph, once this length is reached, the next value will go back to the start
* minValue - the minimum value the bar graph should display, any values less than this will show as zero blocks
* maxValue - the maximum value the bar graph should display, any value greater than this will show as the maximum height in blocks

Based on the height, minValue and maxValue the BarGraph will scale the number of blocks

The BarGraph has 2 methods:

* addValue(value) - add 1 value to the BarGraph
* clear() - clears the BarGraph

::

    from spacecraft.mcsensors import BarGraph
    from mcpi.minecraft import Minecraft
    from time import sleep

    #create connection to minecraft
    mc = Minecraft.create()
    #find the players position
    pos = mc.player.getTilePos()

    #create the bar graph
    height = 20
    maxLength = 10
    minValue = 0
    maxValue = 20
    graph = BarGraph(mc, pos, height, maxLength, minValue, maxValue)

    #add some values to the bar graph
    for value in range(0,20):
        graph.addValue(value)
        sleep(1)

    graph.clear()

Optionally the following parameters can also be used when creating the BarGraph:

* blocksToUse - a list of mcpi.block.Block objects for the blocks which should be used in the bar graph, by default the bar graph will use the 16 colours of wool blocks
* xIncrement - a value to increment pos.x by each time a value is added to the bar graph, by default this value is 1 meaning each value added to the BarGraph makes the grap
* zIncrement - a value to increment pos.z by ...  

::

    from spacecraft.mcsensors import BarGraph
    from mcpi.minecraft import Minecraft
    from mcpi import block
    from mcpi.block import Block
    from time import sleep

    mc = Minecraft.create()
    pos = mc.player.getTilePos()
    height = 20
    maxLength = 10
    minValue = 0
    maxValue = 20
    blocksToUse = [Block(block.STONE.id), Block(block.WOOL.id, 3)]
    xIncrement = 0
    zIncrement = 1

    graph = BarGraph(mc, pos, height, maxLength, minValue, maxValue, blocksToUse, xIncrement, zIncrement)

    for value in range(0,20):
        graph.addValue(value)

    graph.clear()

By modifying xIncrement and zIncrement a bar graph can be made to go in any direction.

SpikeyCircle
````````````
To create a SpikeyCircle the minimum values which have to be passed are:

* mc - minecraft connection
* pos - position to create the SpikeyCircle
* maxRadius - the maximum radius that the lines of the Spikey Circle will go out
* minValue - the minimum value the spikey circle should display, any values less than this will show as zero blocks
* maxValue - the maximum value the spikey circle should display, any value greater than this will show as the maximum radius in blocks

Based on the maxRadius, minValue and maxValue the SpikeyCircle will scale the number of blocks

The SpikeyCircle has 2 methods:

* addValue(value) - add 1 value to the SpikeyCircle
* clear() - clears the SpikeyCircle

::

    from spacecraft.mcsensors import SpikeyCircle
    from mcpi.minecraft import Minecraft
    from mcpi import block
    from mcpi.block import Block
    from time import sleep

    #create connection to minecraft
    mc = Minecraft.create()
    #find the players position
    pos = mc.player.getTilePos()

    #create the spikey circle
    maxRadius = 20
    minValue = 0
    maxValue = 30
    circle = SpikeyCircle(mc, pos, maxRadius, minValue, maxValue)

    #add some values to the spikey circle
    for value in range(0,30):
        circle.addValue(value)
        sleep(1)

    circle.clear()

Optionally the following parameters can also be used when creating the BarGraph:

* blocksToUse - a list of mcpi.block.Block objects for the blocks which should be used in the spikey circle, by default the spikey circle will use the 16 colours of wool blocks
* angleIncrement - an angle to increment by each time a new line is drawn, by default its 15

::

    from spacecraft.mcsensors import SpikeyCircle
    from mcpi.minecraft import Minecraft
    from time import sleep

    #create connection to minecraft
    mc = Minecraft.create()
    #find the players position
    pos = mc.player.getTilePos()

    #create the spikey circle
    maxRadius = 20
    minValue = 0
    maxValue = 30
    blocksToUse = [Block(block.STONE.id), Block(block.WOOL.id, 3)]
    angleIncrement = 10
    circle = SpikeyCircle(mc, pos, maxRadius, minValue, maxValue, blocksToUse, angleIncrement)

    #add some values to the spikey circle
    for value in range(0,30):
        circle.addValue(value)
        sleep(1)

    circle.clear()

Contributors
============

* Hannah Belshaw
* `Martin O'Hanlon`_

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
.. _Stuff about=code: http://www.stuffaboutcode.com
.. _CSV: http://en.wikipedia.org/wiki/Comma-separated_values
.. _Minecraft Pi Edition: http://pi.minecraft.net
.. _Primary School Winning Entry: http://www.ukspace.org/news-item/uk-primary-students-win-competition-to-send-experiments-into-space/
