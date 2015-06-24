from mcpi.minecraft import Minecraft
from mcmodels import Rocket, LaunchPad
from time import sleep
import math

def findPointOnCircle(cx, cy, radius, angle):
    x = cx + math.sin(math.radians(angle)) * radius
    y = cy + math.cos(math.radians(angle)) * radius
    return((int(x + 0.5),int(y + 0.5)))

if __name__ == "__main__":

    mc = Minecraft.create()

    mc.postToChat("SpaceCRAFT - Minecraft Rocket Launch")
    mc.postToChat("Hit the launch pad")
    
    #create the rocket next to the player at ground level
    rocketPos = mc.player.getTilePos()
    rocketPos.x += 5
    rocketPos.y = mc.getHeight(rocketPos.x, rocketPos.z) - 1
    rocket = Rocket(mc, rocketPos)
    launchpad = LaunchPad(mc, rocketPos)
    
    try:
        #wait till the launch tnt is hit
        launch = False
        while not launch:
            for hit in mc.events.pollBlockHits():
                shapeblockhit = launchpad.getShapeBlock(
                    hit.pos.x, hit.pos.y, hit.pos.z)
                
                if shapeblockhit != None:
                    
                    if shapeblockhit.tag == "launch":
                        launch = True
                
        #count down to blast off
        for count in range(3, 0, -1):
            mc.postToChat(str(count))
            sleep(1)
        mc.postToChat("Blast Off")

        #launch the rocket
        for up in range(0, 10):
            rocket.moveBy(0, 1, 0)
            
        #pitch the rocket over
        pitch = 0
        for up in range(0, 75):
            #find out where the rocket should be pointing for its pitch
            z, y = findPointOnCircle(0, 0, 1, pitch)
            #rotate the rocket
            rocket.rotate(0, pitch, 0)
            #move the rocket
            rocket.moveBy(0, y, z)
            #increase the angle of pitch until it gets to 60 degrees
            if pitch < 60: pitch += 3
      
    finally:
        rocket.clear()
        launchpad.clear()
        
