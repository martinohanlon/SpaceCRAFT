from mcpi.minecraft import Minecraft
from mcpi import block
from mcmodels import ISS
from mcdisplaytube import DisplayTube
from astro_pi import AstroPi
from time import sleep

"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

mcdisplays.py

Displays information from the Astro Pi in Minecraft
"""

class ISSTowerMinecraftDisplay():
    """
    A minecraft display which is 3 towers showing sensor data leading up to
    the ISS
    """
    def __init__(self, mc, pos):
        #calculate the positions of the towers
        temppos = pos.clone()
        temppos.x += 3

        humiditypos = pos.clone()
        humiditypos.x -= 3

        pressurepos = pos.clone()
        pressurepos.z += 3
        
        #create the tubes
        self.tempTube = DisplayTube(mc, tempTubePos, 20,
                                    10, 40,
                                    block.LAVA.id)

        self.humidityTube = DisplayTube(mc, humidTubePos, 20,
                                        20, 45,
                                        block.WATER)

        self.pressureTube = DisplayTube(mc, pressureTubePos, 20,
                                        950, 1050,
                                        block.OBSIDIAN)

        #create the ISS

    def update(self, temperature, humidity, pressure, orientation):
        #update the display
        self.tempTube.setValue(temperature)
        self.humidityTube.setValue(humidity)
        self.pressureTube.setValue(pressure)

    def clear(self)
        #clear the display
        self.tempTube.clear()
        self.humidTube.clear()
        self.pressureTube.clear()

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
if __name__ = "__main__":
    mcdisplay = AstroPiMinecraftDisplay()
    try:
        mcdisplay.update(30, 40, 1000, {"yaw": 0, "pitch": 0, "roll": 0})
    finally
        mcdisplay.clear()
    
    
