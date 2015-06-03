"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

mcclock.py

Displays a clock in Minecraft
"""

from time import time, gmtime, sleep
from mcpi.minecraft import Minecraft
from mcpi import block

DIGITS = {
    "1":
    " # " + "\n" +
    "## " + "\n" +
    " # " + "\n" +
    " # " + "\n" +
    "###" + "\n",
    "2":
    "###" + "\n" +
    "  #" + "\n" +
    "###" + "\n" +
    "#  " + "\n" +
    "###" + "\n",
    "3":
    "###" + "\n" +
    "  #" + "\n" +
    "###" + "\n" +
    "  #" + "\n" +
    "###" + "\n",
    "4":
    "#  " + "\n" +
    "#  " + "\n" +
    "# #" + "\n" +
    "###" + "\n" +
    "  #" + "\n",
    "5":
    "###" + "\n" +
    "#  " + "\n" +
    "###" + "\n" +
    "  #" + "\n" +
    "###" + "\n",
    "6":
    "###" + "\n" +
    "#  " + "\n" +
    "###" + "\n" +
    "# #" + "\n" +
    "###" + "\n",
    "7":
    "###" + "\n" +
    "  #" + "\n" +
    " # " + "\n" +
    " # " + "\n" +
    "#  " + "\n",
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
    " ":
    "   " + "\n" +
    "   " + "\n" +
    "   " + "\n" +
    "   " + "\n" +
    "   " + "\n",
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
    "#  " + "\n" +
    "#  " + "\n",
    ":":
    "   " + "\n" +
    " # " + "\n" +
    "   " + "\n" +
    " # " + "\n" +
    "   " + "\n"}

DIGITWIDTH = 3
DIGITHEIGHT = 5
DIGITBLOCKID = block.WOOL.id
DIGITBLOCKDATA = 11

class MinecraftClock():

    def __init__(self, mc, pos):
        self.mc = mc
        self.pos = pos

        #find the positions of the digits
        self.daypos = pos
        self.slash1pos = self._addSpaceToPos(self.daypos, DIGITWIDTH * 2 + 1)
        self.monthpos = self._addSpaceToPos(self.slash1pos, DIGITWIDTH)
        self.slash2pos = self._addSpaceToPos(self.monthpos, DIGITWIDTH * 2 + 1)
        self.yearpos = self._addSpaceToPos(self.slash2pos, DIGITWIDTH)
        
        self.hourpos = self._addSpaceToPos(pos, 0, (DIGITHEIGHT + 1) * -1)
        self.colon1pos = self._addSpaceToPos(self.hourpos, DIGITWIDTH * 2 + 1)
        self.minutepos = self._addSpaceToPos(self.colon1pos, DIGITWIDTH)
        self.colon2pos = self._addSpaceToPos(self.minutepos, DIGITWIDTH * 2 + 1)
        self.secpos = self._addSpaceToPos(self.colon2pos, DIGITWIDTH)
        
        #set up the time properties
        self.year = -1
        self.month = -1
        self.day = -1
        self.hour = -1
        self.minute = -1
        self.second = -1

        self._drawClock()

    def _addSpaceToPos(self, pos, x = 0, y = 0, z = 0):
        newpos = pos.clone()
        newpos.x += x
        newpos.y += y
        newpos.z += z
        return newpos

    def setTime(self, newtime):
        year, month, day, hour, minute, second = self._splitTime(newtime)
        self._drawTime(year, month, day, hour, minute, second)

    def updateTime(self):
        """
        Updates the time on the clock to the current time
        """
        self.setTime(time())

    def _formatNumber(self, number):
        #I want to pad a number with a zero, and make sure its only 2 characters 
        numstr = "0" + str(number)
        return numstr[-2:]

    def _drawClock(self):
        self._drawDigit(self.slash1pos, ".")
        self._drawDigit(self.slash2pos, ".")
        self._drawDigit(self.colon1pos, ":")
        self._drawDigit(self.colon2pos, ":")
        
    def _drawTime(self, year, month, day, hour, minute, second):
        """
        DD/MM/YY
        HH:NN:SS
        """
        if year != self.year:
            self._drawNumber(self.yearpos, self._formatNumber(year))
            self.year = year
        if month != self.month:
            self._drawNumber(self.monthpos, self._formatNumber(month))
            self.month = month
        if day != self.day:
            self._drawNumber(self.daypos, self._formatNumber(day))
            self.day = day
        if hour != self.hour:
            self._drawNumber(self.hourpos, self._formatNumber(hour))
            self.hour = hour
        if minute != self.minute:
            self._drawNumber(self.minutepos, self._formatNumber(minute))
            self.minute = minute
        if second != self.second:
            self._drawNumber(self.secpos, self._formatNumber(second))
            self.second = second

    def _drawNumber(self, topLeftPos, number):
        currentPos = topLeftPos.clone()

        for digit in number:
            self._drawDigit(currentPos, digit)
            currentPos.x += DIGITWIDTH + 1
            
    def _drawDigit(self, topLeftPos, digit):
        #is digit in my list?
        currentPos = topLeftPos.clone()

        if digit in DIGITS.keys():
            #loop through the charactors
            for char in DIGITS[digit]:
                if char == "#":
                    #create a block
                    currentPos.x += 1
                    self.mc.setBlock(currentPos.x, currentPos.y, currentPos.z,
                                     DIGITBLOCKID, DIGITBLOCKDATA)
                elif char == " ":
                    #create a block of air
                    currentPos.x += 1
                    self.mc.setBlock(currentPos.x, currentPos.y, currentPos.z,
                                     block.AIR.id)
                elif char == "\n":
                    currentPos.y -= 1
                    currentPos.x = topLeftPos.x

    def _splitTime(self, thetime):
        #split the time into its bits
        timebits = gmtime(thetime)
        year = timebits.tm_year
        month = timebits.tm_mon
        day = timebits.tm_mday
        hour = timebits.tm_hour
        minute = timebits.tm_min
        second = timebits.tm_sec
        return year, month, day, hour, minute, second
    
    def clear(self):
        self.mc.setBlocks(
            self.pos.x, self.pos.y, self.pos.x,
            self.pos.x + (DIGITWIDTH * 8) + 3, self.pos.y - (DIGITHEIGHT * 2) - 1, self.pos.z,
            block.AIR.id)



if __name__ == "__main__":
    mc = Minecraft.create()
    pos = mc.player.getTilePos()
    pos.y += 10
    try:
        clock = MinecraftClock(mc, pos)
        while True:
            clock.updateTime()
            sleep(0.1)
    finally:
        clock.clear()
