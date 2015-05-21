"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

displaytube.py

A tower of glass blocks in minecraft that can show a value of
blocks up the middle. Think Minecraft thermometer!
"""
from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
from mcpi import block
from time import sleep

class DisplayTube():
    def __init__(
        self,
        mc,
        pos,
        height,
        minValue,
        maxValue,
        blockId,
        blockData = 0):

        self.mc = mc
        self.pos = pos
        self.height = height
        self.minValue = float(minValue)
        self.maxValue = float(maxValue)
        self.numOfBlocks = -1
        self.blockId = blockId
        self.blockData = blockData

        self._buildTube()

    def _buildTube(self):
        """
        Internal. Builds a tube to show the data in
        """
        #create 4 pillars of glass
        self.mc.setBlocks(self.pos.x + 1, self.pos.y, self.pos.z,
                          self.pos.x + 1, self.pos.y + self.height, self.pos.z,
                          block.GLASS.id)
        self.mc.setBlocks(self.pos.x - 1, self.pos.y, self.pos.z,
                          self.pos.x - 1, self.pos.y + self.height, self.pos.z,
                          block.GLASS.id)
        self.mc.setBlocks(self.pos.x, self.pos.y, self.pos.z + 1,
                          self.pos.x, self.pos.y + self.height, self.pos.z + 1,
                          block.GLASS.id)
        self.mc.setBlocks(self.pos.x, self.pos.y, self.pos.z - 1,
                          self.pos.x, self.pos.y + self.height, self.pos.z - 1,
                          block.GLASS.id)
        #put a bottom on it
        self.mc.setBlock(self.pos.x, self.pos.y - 1, self.pos.z, block.GLASS.id)

    def _calcNumOfBlocks(self, value):
        """
        Internal. Calculate how far up the tube the blocks should go based
        on the min, max and height
        """
        scale = self.maxValue - self.minValue
        flatValue = value - self.minValue
        return int(round((flatValue / scale) * self.height))
    
    def setValue(self, value):
        """
        Sets the value in the tube
        """
        self.value = float(value)

        #update the min and max values if this new value is outside them
        if value > self.maxValue: self.maxValue = value
        if value < self.minValue: self.minValue = value        
        
        newNumOfBlocks = self._calcNumOfBlocks(self.value)

        #debug
        #print("value = {}, blocks = {}".format(value, newNumOfBlocks))
        
        #has the number of blocks changed?
        if newNumOfBlocks < self.numOfBlocks:
            #its less so set the blocks at the top to AIR
            self.mc.setBlocks(self.pos.x, self.pos.y + self.numOfBlocks, self.pos.z,
                              self.pos.x, self.pos.y + newNumOfBlocks + 1, self.pos.z,
                              block.AIR.id)
        elif newNumOfBlocks > self.numOfBlocks:
            #its more so set the blocks at the top to the blockType
            self.mc.setBlocks(self.pos.x, self.pos.y + self.numOfBlocks + 1, self.pos.z,
                              self.pos.x, self.pos.y + newNumOfBlocks, self.pos.z,
                              self.blockId, self.blockData)

        self.numOfBlocks = newNumOfBlocks
         
    def clear(self):
        """
        Clears the tube from minecraft
        """
        self.mc.setBlocks(self.pos.x + 1, self.pos.y, self.pos.z,
                          self.pos.x + 1, self.pos.y + self.height, self.pos.z,
                          block.AIR.id)
        self.mc.setBlocks(self.pos.x - 1, self.pos.y, self.pos.z,
                          self.pos.x - 1, self.pos.y + self.height, self.pos.z,
                          block.AIR.id)
        self.mc.setBlocks(self.pos.x, self.pos.y, self.pos.z + 1,
                          self.pos.x, self.pos.y + self.height, self.pos.z + 1,
                          block.AIR.id)
        self.mc.setBlocks(self.pos.x, self.pos.y, self.pos.z - 1,
                          self.pos.x, self.pos.y + self.height, self.pos.z - 1,
                          block.AIR.id)
        self.mc.setBlocks(self.pos.x, self.pos.y, self.pos.z,
                          self.pos.x, self.pos.y + self.height, self.pos.z,
                          block.AIR.id)
        self.mc.setBlock(self.pos.x, self.pos.y - 1, self.pos.z, block.AIR.id)

#test
if __name__ == "__main__":
    mc = Minecraft.create()
    pos = Vec3(0,10,0)
    tube = DisplayTube(mc, pos, 10, 0, 10, 0, block.LAVA.id)
    try:
        sleep(5)
        for count in range(0,11):
            print(count)
            tube.setValue(count)
            sleep(1)
        for count in range(10,0,-1):
            tube.setValue(count)
            sleep(1)
    finally:
        tube.clear()
