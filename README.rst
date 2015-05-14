=========
SpaceCRAFT
=========

Description. Conceived by Hannah Belshaw, from Cumnor House Girl’s School, created by Martin O'Hanlon, www.stuffaboutcode.com.

Installation
============

Todo

Structure
============

* datalogger - used to gather data from the astro pi sense hat and write it to a CSV file
* poc - proof of concept code used in the development
* scripts - useful scripts!

Usage
=====

Data logger
----------

The datalogger/astropidatalogger.py program is run using::

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

    sudo python astropidatalogger.py /home/pi/datafile.csv 180 1

Documentation
============

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
