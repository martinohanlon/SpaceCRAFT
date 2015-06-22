"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

mcsensors.py

A collection of minecraft objects which can display sensor data

A tower of glass blocks in minecraft that can show a value of
blocks up the middle. Think Minecraft thermometer!
"""
from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
from mcpi import block
from mcpi.block import Block
from minecraftstuff import MinecraftShape, MinecraftDrawing
from time import sleep
from math import sin, cos, radians, sqrt

class BarGraph():
    """
    A bar graph in minecraft
    """
    def __init__(
        self,
        mc,
        pos,
        height,
        maxLength,
        minValue,
        maxValue,
        blocksToUse = None,
        xIncrement = 1,
        zIncrement = 0):

        #store the values of the bar graph
        self.mc = mc
        self.pos = pos
        self.height = height
        self.maxLength = maxLength
        self.minValue = minValue
        self.maxValue = maxValue
        if blocksToUse == None:
            blocksToUse = []
            for col in range(0,15):
                blocksToUse.append(Block(block.WOOL.id, col))
        self.blocksToUse = blocksToUse
        self.xIncrement = xIncrement
        self.zIncrement = zIncrement
        self.currentBlock = 0

        #set the position of the next bar in the graph
        self.barPos = pos.clone()
        
        self.graphLength = 0

    def addValue(self, value):
        """
        Add a single value to the bar graph
    `   """
        if value > self.maxValue: value = self.maxValue
        if value < self.minValue: value = self.minValue

        #calculate how far up the block go
        numOfBlocksUp = self._calcNumOfBlocks(value)

        #do the bottom of the bar graph
        self.mc.setBlocks(
            self.barPos.x, self.barPos.y, self.barPos.z,
            self.barPos.x, self.barPos.y + numOfBlocksUp, self.barPos.z,
            self.blocksToUse[self.currentBlock].id, self.blocksToUse[self.currentBlock].data)

        #do the top of the bar graph
        self.mc.setBlocks(
            self.barPos.x, self.barPos.y + numOfBlocksUp + 1, self.barPos.z,
            self.barPos.x, self.barPos.y + self.height, self.barPos.z,
            block.AIR.id)
        
        #increment the graph pos
        self._incrementGraphPos()

        #increment the block type
        self._incrementBlock()

    def _incrementGraphPos(self):
        #increment the length and reset if its over the maximum
        self.graphLength += 1
        if self.graphLength == self.maxLength:
            self.graphLength = 0
            self.barPos = pos.clone()
        else:
            #move the bar on
            self.barPos.x += self.xIncrement
            self.barPos.z += self.zIncrement

    def _incrementBlock(self):
        #increment the block
        self.currentBlock += 1

        #if its the end, go back to the start 
        if self.currentBlock + 1 > len(self.blocksToUse):
            self.currentBlock = 0

    def clear(self):
        """
        Clears the bar graph
    `   """
        self.mc.setBlocks(
            self.pos.x,
            self.pos.y,
            self.pos.z,
            self.pos.x + (self.maxLength * self.xIncrement),
            self.pos.y + self.height,
            self.pos.x + (self.maxLength * self.zIncrement),
            block.AIR.id)

    def _calcNumOfBlocks(self, value):
        """
        Internal. Calculate how far up the graph the blocks should go based
        on the min, max and height
        """
        scale = self.maxValue - self.minValue
        flatValue = value - self.minValue
        return int(round((flatValue / scale) * self.height))

class DisplayTube():
    """
    A tower of glass blocks in minecraft that can show a value of
    blocks up the middle. Think Minecraft thermometer!
    """
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

        self.value = None

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

        #has the value changed?
        if self.value != value:
            
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


class SpikeyCircle():
    """
    Draws lines out from the centre, the lenght determines the value, the longer the line the greater the value
    """
    ANGLEINCREMENT = 15
    
    def __init__(
        self,
        mc,
        pos,
        maxRadius,
        minValue,
        maxValue,
        blocksToUse = None,
        angleIncrement = ANGLEINCREMENT):

        self.mc = mc
        self.pos = pos
        self.maxRadius = maxRadius
        self.minValue = minValue
        self.maxValue = maxValue

        #if no blocks to use have been passed, set them to the wool colours
        if blocksToUse == None:
            blocksToUse = []
            for col in range(0,15):
                blocksToUse.append(Block(block.WOOL.id, col))
                
        self.blocksToUse = blocksToUse
        self.angleIncrement = angleIncrement
        self.currentBlock = 0
        self.angle = 0

        #create a dictionary of the lines for the angles in the circle
        # to keep track of the values so they can be cleared
        self.lines = {}

        #create the minecraft drawing object which will be used to draw the lines
        self.draw = MinecraftDrawing(mc)

    def addValue(self, value):
        """
        Add a single value to the spikey circle
    `   """
        if value > self.maxValue: value = self.maxValue
        if value < self.minValue: value = self.minValue

        #has a line already been drawn at this angle
        if self.angle in self.lines:        
            #clear the line
            endX = self.lines[self.angle][0]
            endY = self.lines[self.angle][1]
            self.draw.drawLine(
                self.pos.x, self.pos.y, self.pos.z,
                endX, endY, self.pos.z,
                block.AIR.id)

        #calculate the length of the line
        lineLen = self._calcLength(value)

        #calculate the new end of the line
        endX, endY = self._findPointOnCircle(
            self.pos.x, self.pos.y,
            self.angle, lineLen)
        
        #draw the line
        self.draw.drawLine(
            self.pos.x, self.pos.y, self.pos.z,
            endX, endY, self.pos.z,
            self.blocksToUse[self.currentBlock].id,
            self.blocksToUse[self.currentBlock].data)

        #save the line to the dictionary, so next time we can clear it
        self.lines[self.angle] = [endX, endY]

        #increment the angle
        self._incrementAngle()

        #increment the block
        self._incrementBlock()

    def _incrementBlock(self):
        #increment the block
        self.currentBlock += 1

        #if its the end, go back to the start 
        if self.currentBlock + 1 > len(self.blocksToUse):
            self.currentBlock = 0

    def _incrementAngle(self):
        #increment the angle
        self.angle += self.angleIncrement

        #if its over 360 go back to the start 
        if self.angle >= 360:
            self.angle -= 360
    
    def _calcLength(self, value):
        scale = self.maxValue - self.minValue
        flatValue = value - self.minValue
        return int(round((flatValue / scale) * self.maxRadius))

    def _findPointOnCircle(self, cx, cy, angle, radius):
        x = cx + sin(radians(angle)) * radius
        y = cy + cos(radians(angle)) * radius
        x = int(round(x, 0))
        y = int(round(y, 0))
        return(x,y)

    def clear(self):
        """
        Clears the spikey circle
    `   """
        for angle in self.lines:
            endX = self.lines[angle][0]
            endY = self.lines[angle][1]
            self.draw.drawLine(
                self.pos.x, self.pos.y, self.pos.z,
                endX, endY, self.pos.z,
                block.AIR.id)

        #reset
        self.angle = 0
        self.currentBlock = 0
#test                
if __name__ == "__main__":

    mc = Minecraft.create()
    pos = Vec3(0,100,0)
    mc.player.setTilePos(5,100,5)
    circle = SpikeyCircle(mc, pos, 20, 0, 30)
    try:
        sleep(1)
        for count in range(10,30):
            print(count)
            circle.addValue(count)
            sleep(0.5)
        for count in range(10,0,-1):
            circle.addValue(count)
            sleep(0.5)
    finally:
        circle.clear()

if __name__ == "__main__displaytube":
    mc = Minecraft.create()
    pos = mc.player.getTilePos()
    tube = DisplayTube(mc, pos, 10, 0, 10, block.LAVA.id)
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

if __name__ == "__main__bargraph":

    mc = Minecraft.create()
    pos = mc.player.getTilePos()
    
    tube = BarGraph(mc, pos, 20, 30, 0, 40)
    try:
        sleep(1)
        for count in range(0,40):
            print(count)
            tube.addValue(count)
            sleep(0.2)
        for count in range(10,0,-1):
            tube.addValue(count)
            sleep(0.2)
    finally:
        tube.clear()
