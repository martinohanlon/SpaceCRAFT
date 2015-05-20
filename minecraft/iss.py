"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

iss.py

A movable minecraft model of the ISS
"""

from minecraftstuff import MinecraftShape
from minecraftstuff import ShapeBlock
from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
from mcpi import block
from time import sleep

class ISS(MinecraftShape):
    def __init__(self, mc, pos):

        self.pos = pos
        self.mc = mc

        #init the MinecraftShape
        MinecraftShape.__init__(self, self.mc, self.pos, visible = False)

        #create the ISS using setBlock(s) commands
        # an arrow
        self.setBlocks(0, 0, -5, 0, 0, 5, block.WOOL.id, 1)
        self.setBlocks(1, 0, -4, 1, 0, -4, block.WOOL.id, 2)
        self.setBlocks(-1, 0, -4, -1, 0, -4, block.WOOL.id, 2)
        self.setBlocks(2, 0, -3, 2, 0, -3, block.WOOL.id, 3)
        self.setBlocks(-2, 0, -3, -2, 0, -3, block.WOOL.id, 3)
        self.setBlocks(3, 0, -2, 3, 0, -2, block.WOOL.id, 4)
        self.setBlocks(-3, 0, -2, -3, 0, -2, block.WOOL.id, 4)
        
        #make the iss visible
        self.draw()
    
#test
if __name__ == "__main__":

    mc = Minecraft.create()

    pos = Vec3(0, 20, 0)

    iss = ISS(mc, pos)
    
    try:
        sleep(5)
        iss.rotate(90, 0, 0)
        sleep(5)
    finally:
        iss.clear()
