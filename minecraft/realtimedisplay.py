from iss import ISS
from astro_pi import AstroPi
from time import sleep
from mcpi.minecraft import Vec3

ROUNDINGFACTOR = 15

def roundDeg(number):
    return round((number / ROUNDINGFACTOR),0) * ROUNDINGFACTOR

ap = AstroPi()
ap.set_imu_config(True, True, True)

pos = Vec3(0, 20, 0)
iss = ISS(pos)

try:

    while(True):
        orientation = ap.get_orientation_degrees()
        yaw, pitch, roll = orientation["yaw"], orientation["pitch"], orientation["roll"]
        yaw, pitch, roll = roundDeg(yaw), roundDeg(pitch), roundDeg(roll)
        print("yaw = {}; pitch = {}; roll = {}".format(yaw, pitch, roll))
        #print("yaw = {}; pitch = {}; roll = {}".format(orientation["yaw"], orientation["pitch"], orientation["pitch"]))
        iss.rotate(yaw, pitch, roll)
        sleep(0.1)

finally:
    iss.clear()
