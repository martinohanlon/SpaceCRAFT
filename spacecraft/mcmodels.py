"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

mcmodels.py

A collections of models which can be used in minecraft

"""
from minecraftstuff import MinecraftShape
from minecraftstuff import ShapeBlock
from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
from mcpi import block
from time import sleep

class ISS(MinecraftShape):
    """
    A movable minecraft model of the ISS
    """
    def __init__(self, mc, pos):

        self.pos = pos
        self.mc = mc

        #init the MinecraftShape
        MinecraftShape.__init__(self, self.mc, self.pos, visible = False)

        #create the ISS using setBlock(s) commands
        
        #main body
        self.setBlocks(-2, 0, -16, -2, 0, 16, 42)
        self.setBlocks(-1, -1, 16, -1, -1, -16, 42)
        self.setBlocks(0, -2, -16, 0, -2, 16, 42)
        self.setBlocks(1, -1, 16, 1, -1, -16, 42)
        self.setBlocks(2, 0, -16, 2, 0, 16, 42)
        self.setBlocks(1, 1, 16, 1, 1, -16, 42)
        self.setBlocks(0, 2, -16, 0, 2, 16, 42)
        self.setBlocks(-1, 1, 16, -1, 1, -16, 42)
        self.setBlocks(1, 0, -17, -1, 0, -17, 42)
        self.setBlocks(0, 1, -17, 0, -1, -17, 42)
        self.setBlocks(0, 1, 17, 0, -1, 17, 42)
        self.setBlocks(-1, 0, 17, 1, 0, 17, 42)
        #across 
        self.setBlocks(-12, -1, 0, 7, -1, 0, 42)
        self.setBlocks(-12, 0, 1, 8, 0, 1, 42)
        self.setBlocks(7, 1, 0, -12, 1, 0, 42)
        self.setBlocks(-12, 0, -1, 8, 0, -1, 42)
        self.setBlock(-13, 0, 0, 42)
        #bit on top of the across
        self.setBlock(-13, 0, 0, 42)
        self.setBlock(-10, 1, -1, 42)
        self.setBlock(-10, 2, 0, 42)
        self.setBlock(-10, 1, 1, 42)
        self.setBlock(-5, 1, 1, 42)
        self.setBlock(-5, 1, -1, 42)
        #central spire
        self.setBlocks(-1, 2, 0, -1, 4, 0, 42)
        self.setBlocks(0, 3, -1, 0, 4, -1, 42)
        self.setBlocks(1, 2, 0, 1, 4, 0, 42)
        self.setBlocks(0, 3, 1, 0, 4, 1, 42)
        self.setBlock(0, 5, 0, 42)
        #the T
        self.setBlocks(7, 1, -5, 7, 1, 4, 42)
        self.setBlocks(8, 0, 4, 8, 0, -5, 42)
        self.setBlocks(6, 0, -5, 6, 0, 4, 42)
        self.setBlocks(7, -1, 4, 7, -1, -5, 42)
        self.setBlock(7, 0, -6, 42)
        self.setBlock(7, 0, 5, 42)
        #solar panel supports
        self.setBlocks(14, 0, 14, 3, 0, 14, 42)
        self.setBlocks(3, 0, 9, 14, 0, 9, 42)
        self.setBlocks(14, 0, -10, 3, 0, -10, 42)
        self.setBlocks(3, 0, -14, 14, 0, -14, 42)
        self.setBlocks(-3, 0, -14, -15, 0, -14, 42)
        self.setBlocks(-15, 0, -10, -3, 0, -10, 42)
        self.setBlocks(-3, 0, 9, -14, 0, 9, 42)
        self.setBlocks(-14, 0, 14, -3, 0, 14, 42)
        #solar panels
        self.setBlocks(-4, 0, 15, -15, 0, 15, 35, 1)
        self.setBlocks(-15, 0, 13, -4, 0, 13, 35, 1)
        self.setBlocks(-4, 0, 10, -15, 0, 10, 35, 1)
        self.setBlocks(-15, 0, 8, -4, 0, 8, 35, 1)
        self.setBlocks(-4, 0, -9, -16, 0, -9, 35, 1)
        self.setBlocks(-16, 0, -11, -4, 0, -11, 35, 1)
        self.setBlocks(-4, 0, -13, -16, 0, -13, 35, 1)
        self.setBlocks(-16, 0, -15, -4, 0, -15, 35, 1)
        self.setBlocks(4, 0, -15, 15, 0, -15, 35, 1)
        self.setBlocks(15, 0, -13, 4, 0, -13, 35, 1)
        self.setBlocks(4, 0, -11, 15, 0, -11, 35, 1)
        self.setBlocks(15, 0, -9, 4, 0, -9, 35, 1)
        self.setBlocks(4, 0, 8, 15, 0, 8, 35, 1)
        self.setBlocks(15, 0, 10, 4, 0, 10, 35, 1)
        self.setBlocks(4, 0, 13, 15, 0, 13, 35, 1)
        self.setBlocks(15, 0, 15, 4, 0, 15, 35, 1)

        #make the iss visible
        self.draw()

class Arrow(MinecraftShape):
    """
    A movable arrow minecraft model
    """
    def __init__(self, mc, pos):

        self.pos = pos
        self.mc = mc

        #init the MinecraftShape
        MinecraftShape.__init__(self, self.mc, self.pos, visible = False)

        #create the arrow using setBlock(s) commands
        # an arrow
        self.setBlocks(0, 0, -5, 0, 0, 5, block.WOOL.id, 1)
        self.setBlocks(1, 0, -4, 1, 0, -4, block.WOOL.id, 2)
        self.setBlocks(-1, 0, -4, -1, 0, -4, block.WOOL.id, 2)
        self.setBlocks(2, 0, -3, 2, 0, -3, block.WOOL.id, 3)
        self.setBlocks(-2, 0, -3, -2, 0, -3, block.WOOL.id, 3)
        self.setBlocks(3, 0, -2, 3, 0, -2, block.WOOL.id, 4)
        self.setBlocks(-3, 0, -2, -3, 0, -2, block.WOOL.id, 4)
        
        #make the arrow visible
        self.draw()

class MCAstroPi(MinecraftShape):
    """
    A movable model of the astro pi computer
    """
    def __init__(self, mc, pos):

        self.pos = pos
        self.mc = mc

        #init the MinecraftShape
        MinecraftShape.__init__(self, self.mc, self.pos, visible = False)

        #create the AstroPi using setBlock(s) commands
        
        #boards
        self.setBlocks(-6, -3, -9, 7, -3, 11, 35, 13, tag = "rpi_board")
        self.setBlocks(-6, 0, -9, 7, 0, 6, 35, 13, tag = "astropi_board")
        #pillars
        self.setBlocks(-6, -2, -9, -6, -1, -9, 42)
        self.setBlocks(7, -2, -9, 7, -1, -9, 42)
        self.setBlocks(-6, -2, 6, -6, -1, 6, 42)
        self.setBlocks(7, -2, 6, 7, -1, 6, 42)
        #gpio headers
        self.setBlocks(7, 1, -8, 7, 1, 5, 35, 15, tag = "astropi_gpio")
        self.setBlocks(7, -2, -8, 7, -1, 5, 35, 15, tag = "rpi_gpio")
        #usb and ethernet port
        self.setBlocks(4, -2, 8, 6, 0, 11, 42, tag = "usb")
        self.setBlocks(0, -2, 8, 2, 0, 11, 42, tag = "usb" )
        self.setBlocks(-5, -2, 8, -2, 0, 11, 42, tag = "ethernet")
        #camera, display, power, hdmi, composite ports
        self.setBlocks(-5, -2, 1, -2, -2, 1, 35, 15, tag = "camera")
        self.setBlocks(2, -2, -9, -1, -2, -9, 35, 15, tag = "display")
        self.setBlocks(-6, -2, -7, -6, -2, -6, 42, tag = "power")
        self.setBlocks(-6, -2, -2, -6, -2, 0, 42, tag = "hdmi")
        self.setBlock(-6, -2, 3, 35, 15, tag = "composite")
        #processor
        self.setBlocks(0, -2, -2, 2, -2, -4, 35, 15, tag = "processor")
        #led grid
        self.setBlocks(-3, 1, -8, 4, 1, -1, 35, 0, tag = "led")
        #other astro pi components
        self.setBlocks(3, 1, 1, 4, 1, 2, 35, 15, tag = "level_shifter")
        self.setBlocks(3, 1, 4, 4, 1, 5, 35, 15, tag = "atmel" )
        self.setBlocks(0, 1, 1, 0, 1, 2, 35, 15, tag = "orientation")
        self.setBlock(1, 1, 5, 35, 15, tag = "humidity")
        self.setBlock(-1, 1, 5, 35, 15, tag = "pressure")
        self.setBlock(-2, 1, 3, 35, 15, tag = "eeprom")
        self.setBlocks(-6, 1, -5, -5, 1, -4, 35, 15, tag = "led_driver")
        #astropi joystick
        self.setBlock(-5, 1, 4, 42, tag = "joy_left")
        self.setBlock(-4, 1, 5, 42, tag = "joy_up")
        self.setBlock(-5, 1, 6, 42, tag = "joy_right")
        self.setBlock(-6, 1, 5, 42, tag = "joy_down")
        self.setBlock(-5, 2, 5, 35, 15, tag = "joy_button")
        #astro pi gaps
        self.setBlocks(-1, 0, -9, 2, 0, -9, 0)
        self.setBlocks(-5, 0, 1, -2, 0, 1, 0)
        
        #make the astro pi visible
        self.draw()

class Rocket(MinecraftShape):
    """
    A movable model of a rocket in minecraft
    """
    def __init__(self, mc, pos):

        self.pos = pos
        self.mc = mc

        #init the MinecraftShape
        MinecraftShape.__init__(self, self.mc, self.pos, visible = False)

        #create the arrow using setBlock(s) commands
        #red wool fire!
        self.setBlock(0, 0, 0, 35, 14)
        #block wool wings
        self.setBlocks(-2, 1, 0, 2, 1, 0, 35, 15)
        self.setBlocks(0, 1, 2, 0, 1, -2, 35, 15)
        self.setBlocks(0, 2, -1, 0, 2, 1, 35, 15)
        self.setBlocks(1, 2, 0, -1, 2, 0, 35, 15)
        #white steps on wings
        self.setBlock(-3, 1, 0, 156)
        self.setBlock(-2, 2, 0, 156)
        self.setBlock(0, 1, -3, 156, 2)
        self.setBlock(0, 2, -2, 156, 2)
        self.setBlock(3, 1, 0, 156, 1)
        self.setBlock(2, 2, 0, 156, 1)
        self.setBlock(0, 1, 3, 156, 3)
        self.setBlock(0, 2, 2, 156, 3)
        #white based
        self.setBlocks(1, 3, 0, -1, 3, 0, 155)
        self.setBlocks(0, 3, 1, 0, 3, -1, 155)
        #black band
        self.setBlocks(1, 4, 0, -1, 4, 0, 35, 15)
        self.setBlocks(0, 4, 1, 0, 4, -1, 35, 15)
        #main body
        self.setBlocks(0, 5, -1, 0, 10, -1, 155)
        self.setBlocks(-1, 10, 0, -1, 5, 0, 155)
        self.setBlocks(0, 5, 1, 0, 10, 1, 155)
        self.setBlocks(1, 10, 0, 1, 5, 0, 155)
        #white steps at the top
        self.setBlock(1, 11, 0, 156, 1)
        self.setBlock(0, 11, 1, 156, 3)
        self.setBlock(-1, 11, 0, 156)
        self.setBlock(0, 11, -1, 156, 2)
        #block on the top
        self.setBlock(0, 12, 0, 155)

        
        #make the arrow visible
        self.draw()

#test
if __name__ == "__main__":

    mc = Minecraft.create()

    isspos = Vec3(0, 30, 0)
    #mcastropipos = Vec3(0, 20, 0)

    iss = ISS(mc, isspos)
    #mcastropi = MCAstroPi(mc, mcastropipos)
    
    try:
        sleep(5)

    finally:
        iss.clear()
        #mcastropi.clear()

