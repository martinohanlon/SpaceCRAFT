from mcpi.minecraft import Vec3
from mcpi.minecraft import Minecraft
from mcpi import block
from iss import ISS
from mcastropi import MCAstroPi
from displaytube import DisplayTube
from astro_pi import AstroPi
from time import sleep

ROUNDINGFACTOR = 15

def roundDeg(number):
    return round((number / ROUNDINGFACTOR),0) * ROUNDINGFACTOR

ap = AstroPi()
ap.set_imu_config(True, True, True)

mc = Minecraft.create()
pos = Vec3(0, 5, 0)

issPos = pos.clone()
issPos.z += 10
issPos.y += 5
iss = ISS(mc, issPos)

tempTubePos = pos.clone()
tempTubePos.x -= 5
tempTube = DisplayTube(mc, tempTubePos, 10,
                       25, 40,
                       ap.get_temperature(),
                       block.LAVA.id)

humidTubePos = pos.clone()
humidTube = DisplayTube(mc, humidTubePos, 10,
                        20, 45,
                        ap.get_humidity(),
                        block.WATER)

pressureTubePos = pos.clone()
pressureTubePos.x += 5
pressureTube = DisplayTube(mc, pressureTubePos, 10,
                           950, 1050,
                           ap.get_pressure(),
                           block.OBSIDIAN)

try:

    while(True):
        orientation = ap.get_orientation_degrees()
        yaw, pitch, roll = orientation["yaw"], orientation["pitch"], orientation["roll"]
        yaw, pitch, roll = roundDeg(yaw), roundDeg(pitch), roundDeg(roll)
        #print("yaw = {}; pitch = {}; roll = {}".format(yaw, pitch, roll))
        #print("yaw = {}; pitch = {}; roll = {}".format(orientation["yaw"], orientation["pitch"], orientation["pitch"]))
        iss.rotate(yaw, pitch, roll * -1)
        tempTube.setValue(ap.get_temperature())
        humidTube.setValue(ap.get_humidity())
        sleep(0.1)

finally:
    iss.clear()
    tempTube.clear()
    humidTube.clear()
    pressureTube.clear()
