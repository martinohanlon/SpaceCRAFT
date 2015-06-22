"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

mcastrorealtime.py

Displays information from the Astro Pi board in real time in Minecraft
"""
from mcpi.minecraft import Minecraft
from mcdisplays import ISSTowerMinecraftDisplay
from astropithreaded import AstroPiThreaded
from time import sleep, time
from cputemp import CPUTemp
import pygame
from pygame.locals import *

def init_pygame():
    pygame.init()
    
    pygame.display.set_mode((640, 480))

    pygame.event.set_allowed(KEYUP)

def get_joystick():
    
    up, down, left, right, button = 0, 0, 0, 0, 0
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_DOWN:
                down = 1
            elif event.key == pygame.K_UP:
                up = 1
            elif event.key == pygame.K_LEFT:
                left = 1
            elif event.key == pygame.K_RIGHT:
                right = 1
            elif event.key == pygame.K_RETURN:
                 button = 1
                
    return {"up": up, "down": down, "left": left, "right": right, "button": button}

if __name__ == "__main__":
    #create the connection to minecraft
    mc = Minecraft.create()

    mc.postToChat("SpaceCRAFT - Real time display")
    
    #create the astro pi object, my threaded one which keeps reading orientation data
    ap = AstroPiThreaded()
    ap.set_imu_config(True, True, True)

    #initialise pygame
    init_pygame()

    #open the cpu temperature object
    cpu_temp = CPUTemp()
    cpu_temp.open()

    #find the position of where to put the ISS tower display
    pos = mc.player.getTilePos()
    pos.z -= 10
    pos.y = mc.getHeight(pos.x, pos.z)

    #create the iss tower display
    isstowerdisplay = ISSTowerMinecraftDisplay(mc, pos)
    
    try:
        while True:
            #keep updating the display based on new data
            isstowerdisplay.update(
                time(),
                cpu_temp.get_temperature(),
                ap.get_temperature(),
                ap.get_humidity(),
                ap.get_pressure(),
                ap.get_orientation(),
                get_joystick())
            sleep(0.5)
    finally:
        #clear the display and stop everything
        isstowerdisplay.clear()
        cpu_temp.close()
        ap.stop()
