"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

mcastropi.py

A movable minecraft model of a Raspberry Pi with an Astro Pi on top
"""
from minecraftstuff import MinecraftShape
from minecraftstuff import ShapeBlock
from mcpi.minecraft import Minecraft
from mcpi.minecraft import Vec3
from mcpi import block
from time import sleep

class MCAstroPi(MinecraftShape):
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
    
#test
if __name__ == "__main__":

    mc = Minecraft.create()

    pos = Vec3(0, 20, 0)

    mcastropi = MCAstroPi(mc, pos)
    
    try:
        sleep(5)
        
    finally:
        mcastropi.clear()
