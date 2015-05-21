=========
SpaceCRAFT
=========

IN PROGRESS!!!

Todo. 

Conceived by Hannah Belshaw, from Cumnor House Girl’s School, created by Martin O'Hanlon, `<Stuff about="code" />`_.

Installation
============

Todo

Structure
=========

* spacecraft - spacecraft python module 
* poc - proof of concept code used in the development
* scripts - useful scripts!

Usage
=====

Data logger
-----------

The spacecraft/astropidatalogger.py program reads all the data from the astro pi board and writes it to a CSV files - it is run using::

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

The spacecraft/astropidatareader.py program reads CSV files created by the astropidatalogger.py program, its not invisage it is used to view data, but it provide a methof for testing a file has been created successfully and as well as being an example of how to use the AstroPiDataReader::

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

Todo

Contributors
============

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
.. _Stuff about="code": http://www.stuffaboutcode.com