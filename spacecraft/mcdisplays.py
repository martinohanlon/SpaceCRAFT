from mcpi.minecraft import Minecraft
from mcpi import block
from mcmodels import ISS
from mcsensors import DisplayTube
from time import sleep, time
from mcclock import Clock

"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

mcdisplays.py

Displays information from the Astro Pi in Minecraft
"""

def roundDegrees(number):
    ROUNDDEGREESTO = 15
    return round((number / ROUNDDEGREESTO),0) * ROUNDDEGREESTO

class ISSTowerMinecraftDisplay():
    """
    A minecraft display which is 3 towers showing sensor data leading up to
    the ISS
    """
    def __init__(self, mc, pos):

        self.mc = mc
        self.pos = pos
        
        #calculate the positions of the towers, iss and clock
        temppos = pos.clone()
        temppos.x += 2

        humiditypos = pos.clone()
        humiditypos.x -= 2

        pressurepos = pos.clone()
        pressurepos.z += 2

        isspos = pos.clone()
        isspos.y += 35

        clockpos = pos.clone()
        clockpos.x -= 10
        clockpos.z -= 10
        clockpos.y += 11

        #create the clock
        self.clock = Clock(mc, clockpos, block.WOOL.id, 11)
        
        #create the tubes
        self.tempTube = DisplayTube(mc, temppos, 20,
                                    10, 40,
                                    block.LAVA.id)

        self.humidityTube = DisplayTube(mc, humiditypos, 20,
                                        20, 45,
                                        block.WATER)

        self.pressureTube = DisplayTube(mc, pressurepos, 20,
                                        950, 1050,
                                        block.OBSIDIAN)

        #create the ISS
        self.iss = ISS(mc, isspos)

    def update(self, time, temperature, humidity, pressure, orientation):
        #update the display
        self.clock.setTime(time)
        self.tempTube.setValue(temperature)
        self.humidityTube.setValue(humidity)
        self.pressureTube.setValue(pressure)
        yaw, pitch, roll = orientation["yaw"], orientation["pitch"], orientation["roll"]
        yaw, pitch, roll = roundDegrees(yaw), roundDegrees(pitch), roundDegrees(roll)
        self.iss.rotate(yaw, pitch, roll)

    def clear(self):
        #clear the display
        self.tempTube.clear()
        self.humidityTube.clear()
        self.pressureTube.clear()
        self.iss.clear()
        self.clock.clear()

#TODO
class AbstractMinecraftDisplay():
    """
    An abstract display of the ISS data in Minecraft
    """
    def __init__(self, mc, pos):
        pass

    def update(self, temperature, humidity, pressure, orientation):
        pass

    def clear(self):
        pass
    
#test
if __name__ == "__main__":
    mc = Minecraft.create()
    pos = mc.player.getTilePos()
    pos.y = mc.getHeight(pos.x, pos.y)
    mcdisplay = ISSTowerMinecraftDisplay(mc, pos)
    try:
        mcdisplay.update(time(), 30, 40, 1000, {"yaw": 0, "pitch": 0, "roll": 0})
        sleep(10)
        mcdisplay.update(time(), 20, 30, 1050, {"yaw": 45, "pitch": 90, "roll": 0})
        sleep(10)
    finally:
        mcdisplay.clear()
    
