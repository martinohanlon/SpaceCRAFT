"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

mcclock.py

Displays a clock in Minecraft
"""

from time import time, gmtime

DIGITS = {
    "1":
    " #" + "\n" +
    "##" + "\n" +
    " #" + "\n" +
    " #" + "\n" +
    "###" + "\n",
    "2":
    "###" + "\n" +
    "  #" + "\n" +
    "###" + "\n" +
    "#" + "\n" +
    "###" + "\n",
    "3":
    "###" + "\n" +
    "  #" + "\n" +
    "###" + "\n" +
    "  #" + "\n" +
    "###" + "\n",
    "4":
    "#" + "\n" +
    "#" + "\n" +
    "# #" + "\n" +
    "###" + "\n" +
    "  #" + "\n",
    "5":
    "###" + "\n" +
    "#" + "\n" +
    "###" + "\n" +
    "  #" + "\n" +
    "###" + "\n",
    "6":
    "###" + "\n" +
    "#" + "\n" +
    "###" + "\n" +
    "# #" + "\n" +
    "###" + "\n",
    "7":
    "###" + "\n" +
    "  # " + "\n" +
    " #" + "\n" +
    " #" + "\n" +
    "#" + "\n",
    "8":
    "###" + "\n" +
    "# #" + "\n" +
    "###" + "\n" +
    "# #" + "\n" +
    "###" + "\n",
    "9":
    "###" + "\n" +
    "# #" + "\n" +
    "###" + "\n" +
    "  #" + "\n" +
    "###" + "\n",
    "0":
    "###" + "\n" +
    "# #" + "\n" +
    "# #" + "\n" +
    "# #" + "\n" +
    "###" + "\n",
    ".":
    "   " + "\n" +
    "   " + "\n" +
    "   " + "\n" +
    "   " + "\n" +
    " # " + "\n",
    ",":
    "   " + "\n" +
    "   " + "\n" +
    "   " + "\n" +
    "  #" + "\n" +
    " # " + "\n",
    "/":
    "  #" + "\n" +
    "  #" + "\n" +
    " # " + "\n" +
    "# " + "\n" +
    "# " + "\n",
    ":":
    "   " + "\n" +
    " # " + "\n" +
    "   " + "\n" +
    " # " + "\n" +
    "   " + "\n"}

class MinecraftClock()

    def __init__(self, mc, pos):
        self.mc = mc
        self.pos = pos
        
        self._drawTime(0, 0, 0, 0, 0, 0)

    def setTime(self, newtime):
        #split the time into its bits
        timebits = gmtime(newtime)
        year = timebits.tm_year
        month = timebits.tm_mon
        day = timebits.tm_mday
        hour = timebits.tm_hour
        minute = timebits.tm_min
        second = timebits.tm_sec

    def _drawTime(self, year, month, day, hour, minute, second):
        """
        DD/MM/YY|HH:NN:SS
        """
        pass
    
    def clear(self):
        pass
