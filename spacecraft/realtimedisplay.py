"""
SpaceCRAFT - Astro Pi competition[http://astro-pi.org/] entry
Conceived by Hannah Belshaw
Created by Martin O'Hanlon[http://www.stuffaboutcode.com]
For the Raspberry Pi Foundation[https://www.raspberrypi.org]

realtimedisplay.py

Displays information from the Astro Pi board in real time in Minecraft
"""
from mcpi.minecraft import Vec3
from mcpi.minecraft import Minecraft
from mcpi import block
from mcmodels import ISS
from mcmodels import MCAstroPi
from mcsensors import DisplayTube
from astropithreaded import AstroPiThreaded
from time import sleep

ROUNDINGFACTOR = 15

def roundDeg(number):
    return round((number / ROUNDINGFACTOR),0) * ROUNDINGFACTOR

ap = AstroPiThreaded()
ap.set_imu_config(True, True, True)

mc = Minecraft.create()
pos = mc.player.getTilePos()
pos.y = mc.getHeight(pos.x, pos.z)

#mc.setBlocks(-30, 5, -30, 30, 50, 30, block.AIR.id)

issPos = pos.clone()
issPos.z += 10
issPos.y += 25
iss = ISS(mc, issPos)

tempTubePos = pos.clone()
tempTubePos.x -= 5
tempTube = DisplayTube(mc, tempTubePos, 10,
                       25, 40,
                       block.LAVA.id)

humidTubePos = pos.clone()
humidTube = DisplayTube(mc, humidTubePos, 10,
                        20, 45,
                        block.WATER)

pressureTubePos = pos.clone()
pressureTubePos.x += 5
pressureTube = DisplayTube(mc, pressureTubePos, 10,
                           950, 1050,
                           block.OBSIDIAN)

try:
    lastYaw, lastPitch, lastRoll = 0, 0, 0
    while(True):

        orientation = ap.get_orientation_degrees()
        yaw, pitch, roll = orientation["yaw"], orientation["pitch"], orientation["roll"]
        yaw, pitch, roll = roundDeg(yaw), roundDeg(pitch), roundDeg(roll)
        #print("yaw = {}; pitch = {}; roll = {}".format(yaw, pitch, roll))
        #print("yaw = {}; pitch = {}; roll = {}".format(orientation["yaw"], orientation["pitch"], orientation["pitch"]))
        if yaw != lastYaw or pitch != lastPitch or roll != lastRoll:
            iss.rotate(yaw, pitch, roll * -1)
        lastYaw, lastPitch, lastRoll = yaw, pitch, roll

        tempTube.setValue(ap.get_temperature())
        humidTube.setValue(ap.get_humidity())
        pressureTube.setValue(ap.get_pressure())
        sleep(0.1)

finally:
    iss.clear()
    tempTube.clear()
    humidTube.clear()
    pressureTube.clear()
