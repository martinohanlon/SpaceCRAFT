from mcpi.minecraft import Minecraft
from mcpi import block
from minecraftmodels import ISS
from displaytube import DisplayTube
from astro_pi import AstroPi
from time import sleep

"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

minecraftdisplay.py

Displays information from the Astro Pi in Minecraft
"""

class AstroPiMinecraftDisplay():
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


#test
if __name__ = "__main__":
    mcdisplay = AstroPiMinecraftDisplay()
    try:
        mcdisplay.update(30, 40, 1000, 
    finally
        mcdisplay.clear()
    
    
